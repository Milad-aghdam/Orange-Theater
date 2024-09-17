from django.shortcuts import render
from django.http import  JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required


import json
import time
from bs4 import BeautifulSoup
import datetime

from .models import  BusinessInformation
from .create_service import create_service



def extract_shop_name(content):
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        return soup.find('b').text if soup.find('b') else ''
    return ''

def extract_location_id(content):
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        location_id_tag = soup.find(string=lambda text: 'Location_ID' in text)
        if location_id_tag:
            location_id = location_id_tag.split('Location_ID: ')[1].strip()
            return location_id
    return ''
def get_opening_hours(shop_name, location_id):
    opening_hours = {}
    if shop_name and location_id:
        try:
            business_info = BusinessInformation.objects.get(
                (Q(title__iexact=shop_name) | Q(title__icontains=shop_name)) & Q(name=location_id)
            )
            days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
            for day in days:
                hours = getattr(business_info, day)
                periods = []
                if hours:
                    try:
                        open_times = hours.strip('[]').split('", "')
                        for period in open_times:
                            times = period.split(' - ')
                            if len(times) == 2:
                                periods.append({
                                    'open': times[0].strip('" '),
                                    'close': times[1].strip('" ')
                                })
                    except ValueError:
                        pass
                opening_hours[day] = periods
        except BusinessInformation.DoesNotExist:
            print("No BusinessInformation matches the given shop name and location ID.")
    return opening_hours

def sort_opening_hours_by_current_day(opening_hours):
    current_day_index = (datetime.datetime.today().weekday() + 1) % 7  # Monday is 0 and Sunday is 6
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day_order = days[current_day_index:] + days[:current_day_index]
    sorted_hours = {}
    for day in day_order:
        periods = opening_hours.get(day, [])
        sorted_hours[day] = {
            'periods': periods,
            'has_opening_times': bool(periods)
        }
    return sorted_hours

@login_required
def map_detail(request):
    content = request.GET.get('content', '')
    shop_name = extract_shop_name(content)
    location_id = extract_location_id(content)

    if not shop_name:
        shop_name = request.GET.get('shop_name', '').strip()
    
    if not location_id:
        location_id = request.GET.get('location_id', '').strip()

    print("Extracted Shop Name:", shop_name)
    print("Extracted Location ID:", location_id)

    opening_hours = get_opening_hours(shop_name, location_id)
    sorted_opening_hours = sort_opening_hours_by_current_day(opening_hours)

    # Process the opening hours data to split times into hours and minutes
    for day, data in sorted_opening_hours.items():
        for period in data['periods']:
            period['open_hour'], period['open_minute'] = period['open'].split(':')
            period['close_hour'], period['close_minute'] = period['close'].split(':')

    context = {
        'shop_name': shop_name,
        'location_id': location_id,
        'opening_hours': sorted_opening_hours,
    }

    return render(request, 'googlebusiness/openhours.html', context)

def update_open_hours(google_business_info, location_id, request_body, update_mask="regularHours.periods"):
    max_retries = 3
    retry_delay = 10  # seconds
    for attempt in range(max_retries):
        try:
            request = google_business_info.locations().patch(
                name=location_id,
                updateMask=update_mask,
                body=request_body
            )
            result = request.execute()
  
            break  # Exit loop if successful

        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt+1}/{max_retries}: {e}")
                print("Retrying in {} seconds...".format(retry_delay))
                time.sleep(retry_delay)
            else:
                print("Maximum retries exceeded. Unable to update open hours.")
                raise e


def edit_function(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # print("Received data:", data)

            location_id = data['locationId'].split('|')[0]

            periods = []
            for day, details in data['opening_hours'].items():
                for period in details['periods']:
                    open_time_parts = period['open'].split(':')
                    close_time_parts = period['close'].split(':')

                    periods.append({
                        "openDay": day,
                        "openTime": {
                            "hours": int(open_time_parts[0]),
                            "minutes": int(open_time_parts[1])
                        },
                        "closeDay": day,
                        "closeTime": {
                            "hours": int(close_time_parts[0]),
                            "minutes": int(close_time_parts[1])
                        }
                    })

            request_body = {
                "regularHours": {
                    "periods": periods
                }
            }

            # Assuming you have a function `create_service` to authenticate and create a Google My Business client
            google_business_info = create_service()

            if google_business_info is None:
                return JsonResponse({'status': 'error', 'message': 'Failed to create Google Business client'}, status=500)

            try:
                # Ensure all required arguments are passed
                update_open_hours(google_business_info, location_id, request_body)
            except Exception as e:
                print(f"Error during updating open hours: {e}")
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

            return JsonResponse({
                'status': 'success',
                'message': 'Edit completed!',
                'received_data': data,
                'request_body': request_body,
                'location_id': location_id
            })
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return JsonResponse({'status': 'error', 'message': 'An error occurred'}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

