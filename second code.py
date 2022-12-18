import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Replace the values in this block with your own values
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
refresh_token = 'YOUR_REFRESH_TOKEN'

# Use the refresh token to obtain an access token
creds = Credentials.from_authorized_user_info(info={"client_id": client_id, "client_secret": client_secret, "refresh_token": refresh_token}, scopes=['https://www.googleapis.com/auth/contacts'])

import googleapiclient.discovery

# Create a service object
service = googleapiclient.discovery.build('people', 'v1', credentials=creds)

# Make a request to the People API to retrieve all of the contacts
results = service.people().connections().list(resourceName='people/me', pageSize=2000).execute()

# Get the list of contacts
contacts = results.get('connections', [])


