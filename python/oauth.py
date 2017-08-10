from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from apiclient.discovery import build

scopes = ['https://www.googleapis.com/auth/calendar']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    '/home/tanktankette/Downloads/Community Calendar-eac475d17749.json', scopes=scopes
)

http_auth = credentials.authorize(Http())

calendar = build('calendar', 'v3', http=http_auth)

response = calendar.events().list(calendarId='ministryofmagicpdx@gmail.com',
                                  timeMin='2017-07-31T00:00:00-07:00',
                                  orderBy='startTime',
                                  singleEvents=True).execute()

print(response['items'][0])
