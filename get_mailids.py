import gspread
from random import choice, shuffle
from oauth2client.service_account import ServiceAccountCredentials
from unidecode import unidecode

#authenticating google sheet
def auth_sheet():
    headers = gspread.httpsession.HTTPSession(headers={'Connection':'Keep-Alive'})
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    return client
client = auth_sheet()

# Find a workbook by name and open the first sheet
sender_email_id_sheet = client.open("campaignmails").sheet1
mailbody_sheet = client.open("bodytext").sheet1
mailsubject_sheet = client.open("subjecttext").sheet1
email_leads_sheet = client.open("leads").sheet1

#Collecting data from google sheets
sender_email_ids = sender_email_id_sheet.get_all_records()
mailbodys = mailbody_sheet.get_all_records()
mailsubjects = mailsubject_sheet.get_all_records()
email_leads = email_leads_sheet.get_all_records()


def get_body_text():
    amb = [] #defining an empty list to store all mail body texts
    for row in mailbodys:
        bt = row['texts']
        amb.append(bt)
    shuffle (amb)
    return amb

raw_mail_body = choice(get_body_text())
final_mail_body = str(unidecode(raw_mail_body))


def get_subject_text():
    ams = [] #defining an empty list to store all mail body texts
    for row in mailsubjects:
        st = row['texts']
        ams.append(st)
    shuffle (ams)
    return ams

raw_mail_subject = choice(get_subject_text())
final_mail_subject = str(raw_mail_subject)


def receiver_list():
    receivers = []
    limit_over = "b.(550, b'5.4.5 Daily user sending quota exceeded. m69sm15876126pfk.54 - gsmtp')"
    for row in email_leads:
        lead = row['leads']
        status = row['status']
        #Adding pending email leads only to sending list
        if status == "a.pending" or limit_over:
            receivers.append(lead)
        else:
            break
    return receivers

all_receiver = receiver_list()



# # Handel reporting
# def mailid_err_renew(mialid_row_index, ex):
#     #use creds to create a client to interact with the Google Drive API
#     scope = ['https://spreadsheets.google.com/feeds']
#     creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#     client = gspread.authorize(creds)
#
#     sender_email_id_sheet = client.open("campaignmails").sheet1
#     sender_email_id_sheet.update_cell(mialid_row_index, 5, ex)
#
# def lead_err_renew(lead_row_index, message):
#     # use creds to create a client to interact with the Google Drive API
#     scope = ['https://spreadsheets.google.com/feeds']
#     creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
#     client = gspread.authorize(creds)
#
#     email_leads_sheet = client.open("leads").sheet1
#     email_leads_sheet.update_cell(lead_row_index, 2, message)



# Handel reporting

def mailid_err(mialid_row_index, ex):
    global client
    try:
        sender_email_id_sheet.update_cell(mialid_row_index, 5, ex)
    except:
        client = auth_sheet()
        mailid_err(mialid_row_index, ex)
    

def lead_err(lead_row_index, message):
    global client
    try:
        email_leads_sheet.update_cell(lead_row_index, 2, message)
    except:
        client = auth_sheet()
        lead_err(lead_row_index, message)