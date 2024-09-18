
# google libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient import discovery
from googleapiclient.http import build_http
from oauth2client import client, file, tools
import os 

SCOPES = ['https://www.googleapis.com/auth/business.manage']
CLIENT_SECRETS_FILE = r'.\googlebusiness\docs\client_secrets.json'
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Path to client_secrets.json
# CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'docs', 'client_secrets.json')

# print("Client secrets file path:", CLIENT_SECRETS_FILE)  # Log the path to verify

MYBUSINESSMANAGEMENT_FILE = r'.\googlebusiness\docs\mybusinessbusinessinformation.dat'
# MYBUSINESSMANAGEMENT_FILE = os.path.join(BASE_DIR, 'docs', 'mybusinessbusinessinformation.dat')

def create_service():
    """Fetches business information from Google My Business API."""
    try:
        scope = 'https://www.googleapis.com/auth/business.manage'
        client_secrets = CLIENT_SECRETS_FILE
        flow = client.flow_from_clientsecrets(client_secrets, scope=scope, message=tools.message_if_missing(client_secrets))


        storage = file.Storage(MYBUSINESSMANAGEMENT_FILE)
        credentials = storage.get()
        http = credentials.authorize(http=build_http())
        service = discovery.build("mybusinessbusinessinformation", 'v1', http=http)
        # business_account = service.accounts().list().execute()
        print(service)
        return service

    except HttpError as error:
        print(f'An error occurred: {error}')
        