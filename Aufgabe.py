
import numpy as np
import pandas as pd


import pickle
import os.path
from urllib.error import HTTPError

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

# Call the Gmail API
report_messages = service.users().messages().list(userId='me',q='subject:"Your report is ready"').execute()



# https://stackoverflow.com/questions/25832631/download-attachments-from-gmail-using-gmail-api
# Translated to python3
import base64
from apiclient import errors

def GetAttachments(service, user_id, msg_id):
    """Get and store attachment from Message with given id.

    :param service: Authorized Gmail API service instance.
    :param user_id: User's email address. The special value "me" can be used to indicate the authenticated user.
    :param msg_id: ID of Message containing attachment.
    """
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()

        for part in message['payload']['parts']:
            if part['filename']:
                if 'data' in part['body']:
                    data = part['body']['data']
                else:
                    att_id = part['body']['attachmentId']
                    att = service.users().messages().attachments().get(userId=user_id, messageId=msg_id,id=att_id).execute()
                    data = att['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                path = part['filename']
                print(path)

                with open(path, 'wb') as f:
                    f.write(file_data)

    except HttpError():
        print('An error occurred')


attachments_list = []

for i_message in range(len(report_messages['messages'])):
    message_id = report_messages['messages'][i_message]['id']
    print(message_id)
    GetAttachments(service, 'me', message_id)

service.close()


data_1 = pd.read_csv('2021-02-06-03-04-06-CET-Historical-Report-GUSFacebook-2020-11-06--2021-02-06.csv')
data_2 = pd.read_csv('2021-02-07-03-02-27-CET-Historical-Report-GUSFacebook-2020-11-07--2021-02-07.csv')
data_3 = pd.read_csv('2021-02-08-03-02-18-CET-Historical-Report-GUSFacebook-2020-11-08--2021-02-08.csv')
