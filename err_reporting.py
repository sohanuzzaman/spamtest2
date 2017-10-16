import gspread
from oauth2client.service_account import ServiceAccountCredentials

def mailid_err(row_index):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sender_email_id_sheet = client.open("campaignmails").sheet1
    sender_email_id_sheet.update_cell(row_index, 5, "Problem")

def lead_err(row_index, message):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    email_leads_sheet = client.open("leads").sheet1
    email_leads_sheet.update_cell(row_index, 5, message)