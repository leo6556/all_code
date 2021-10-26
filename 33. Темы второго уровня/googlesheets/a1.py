from pprint import pprint
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CRED_FILE = 'creds.json'
spreadsheets_id = '1DjGp4T1w_ChKieeLKbrNJVFkP6MTwlBbSHiT5u6zeik'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CRED_FILE,
    [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# values = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheets_id,
#     range='A1:E10',
#     majorDimension='ROWS').execute()  # вместо rows можно COLUMNS
# pprint(values)

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheets_id,
    body={
        'valueInputOption' : 'USER_ENTERED',
        'data': [
            {'range' : 'B3:C4',
             'majorDimension' : 'ROWS',
             'values' : [['this is b3', 'this is c3'], ['this is b4', 'this is c4']]},
            {
                'range' : 'D5:E6',
                'majorDimension' : 'COLUMNS',
                'values' : [['no', 'NO'], ['yes', 'YES']]}
        ]
    }
).execute()