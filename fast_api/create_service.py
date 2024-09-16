
# google libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient import discovery
from googleapiclient.http import build_http
from oauth2client import client, file, tools


SCOPES = ['https://www.googleapis.com/auth/business.manage']
CLIENT_SECRETS_FILE = r'.\docs\client_secrets.json'
mybusinessaccountmanagement = r'.\docs\mybusinessaccountmanagement.dat'

def create_service():
    """Fetches business information from Google My Business API."""
    try:
        scope = 'https://www.googleapis.com/auth/business.manage'
        client_secrets = CLIENT_SECRETS_FILE
        flow = client.flow_from_clientsecrets(client_secrets, scope=scope, message=tools.message_if_missing(client_secrets))


        storage = file.Storage(mybusinessaccountmanagement)
        credentials = storage.get()
        http = credentials.authorize(http=build_http())
        service = discovery.build("mybusinessaccountmanagement", 'v1', http=http)
        # business_account = service.accounts().list().execute()
        print(service)
        return service

    except HttpError as error:
        print(f'An error occurred: {error}')
        