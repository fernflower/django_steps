import base64
from email.mime.text import MIMEText
import os
import pickle

from googleapiclient.discovery import build
from googleapiclient import errors
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_creds(token_file, secrets_file, scopes):
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


def get_gmail_service(token_file, secrets_file):
    creds = get_creds(token_file, secrets_file, ['https://www.googleapis.com/auth/gmail.send'])
    return build('gmail', 'v1', credentials=creds)


def send_mail(to, subject, text, service):
    """
    Sends an email with given subject and text to address in to.
    Return HttpError in case of failure.
    """
    message = MIMEText(text)
    message['to'] = to
    message['from'] = 'me'
    message['subject'] = subject
    msg_to_send = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')}
    return service.users().messages().send(userId="me", body=msg_to_send).execute()
