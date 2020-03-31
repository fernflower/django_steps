from __future__ import print_function
import argparse
import datetime
import json
import pickle
import os.path
import sys

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SECRETS_FILE = 'files/credentials.json'
TOKEN_FILE = 'files/token.pickle'


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', default=TOKEN_FILE, help='Token file location')
    parser.add_argument('--count', default=10, help='Number of events to fetch, 10 by default')
    parser.add_argument('--secrets', default=SECRETS_FILE, help='File with google calendar oath credentials location')
    parser.add_argument('--scope', action='append', default=SCOPES,
                        help='Additional scopes to parse, default is {}'.format(SCOPES[0]))
    return parser.parse_args(args)


def _get_creds(token_file, secrets_file, scopes):
    """Get credentials for google calendar access"""

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(secrets_file, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    return creds


def _fetch_eventlist(creds, count):
    """Returns a list of dicts {date, name, description, location}"""

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=count, singleEvents=True,
                                          orderBy='startTime').execute()
    results = []
    for event in events_result.get('items', []):
        start = event['start'].get('dateTime', event['start'].get('date'))
        start_dt = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z")
        # parse date here for the frontend component to use
        start_details = {"month": start_dt.strftime("%b"), "day": start_dt.day, "year": start_dt.year,
                         "time": start_dt.strftime("%H:%M"), "datetime": start_dt.strftime("%Y-%m-%d %H%M")}
        url = next((w for w in event.get('description', '').split() if w.startswith('http')), None)
        location = ('https://www.google.com/maps/search/?api=1&query={}'.format(event['location'])
                    if event.get('location') else None)
        res = {'start': start_details, 'name': event['summary'], 'description': event.get('description', ''),
               'location': location, 'url': url}
        results.append(res)
    return results


def main():
    parsed = parse_args(sys.argv[1:])
    creds = _get_creds(parsed.token, parsed.secrets, parsed.scope)
    events = _fetch_eventlist(creds, parsed.count)
    data = json.dumps(events)
    print(data)

if __name__ == '__main__':
    main()
