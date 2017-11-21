import gspread
from random import choice, shuffle
from oauth2client.service_account import ServiceAccountCredentials
from unidecode import unidecode

#authenticating google sheet
def auth_sheet():
    print("connecting to google sheet...")
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
links_sheet = client.open("links").sheet1

#Collecting data from google sheets
sender_email_ids = sender_email_id_sheet.get_all_records()
mailbodys = mailbody_sheet.get_all_records()
mailsubjects = mailsubject_sheet.get_all_records()
email_leads = email_leads_sheet.get_all_records()
raw_links = links_sheet.get_all_records()

# reconnect google sheet
def update_sheet():
    global client, sender_email_id_sheet, email_leads_sheet
    client = auth_sheet()
    sender_email_id_sheet = client.open("campaignmails").sheet1
    email_leads_sheet = client.open("leads").sheet1


def get_links():
    links = []
    for row in raw_links:
        link = row['links']
        links.append(str(link))
    shuffle (links)
    return links
links = get_links()

def get_body_text():
    print("collecting mail bodys...")
    amb = [] #defining an empty list to store all mail body texts
    for row in mailbodys:
        bt1 = row['texts']
        bt2 = row['texts2']
        url = choice(links)
        bt = str.join(' ', (bt1, url, bt2))
        amb.append(bt)
    shuffle (amb)
    return amb

raw_mail_body = get_body_text()


def get_subject_text():
    print("collecting mail subjects...")
    ams = [] #defining an empty list to store all mail body texts
    for row in mailsubjects:
        st = row['texts']
        ams.append(st)
    shuffle (ams)
    return ams

raw_mail_subject = get_subject_text()

def get_random(mail_text):
    rand_mail_body = choice(raw_mail_body)
    final_mail_body = unidecode(rand_mail_body)
    rand_mail_subject = choice(raw_mail_subject)
    final_mail_subject = unidecode(rand_mail_subject)
    if mail_text == "body":
        return final_mail_body
    else:
        return final_mail_subject


def receiver_list():
    print("collecting leads...")
    receivers = []
    limit_over = "b.(550, b'5.4.5 Daily user sending quota exceeded. m69sm15876126pfk.54 - gsmtp')"
    for row in email_leads:
        lead = row['leads']
        status = row['status']
        #Adding pending email leads only to sending list
        if status == "a.pending" or limit_over:
            receivers.append(lead)
        else:
            continue
    return receivers

all_receiver = receiver_list()


def mailid_err(mialid_row_index, ex):
    try:
        sender_email_id_sheet.update_cell(mialid_row_index, 6, ex)
    except:
        update_sheet()
        mailid_err(mialid_row_index, ex)


# def mailid_ip(mialid_row_index, ip):
#
#     sender_email_id_sheet.update_cell(mialid_row_index, 7, ip)

    

def lead_err(lead_row_index, message):
    try:
        email_leads_sheet.update_cell(lead_row_index, 2, message)
    except:
        update_sheet()
        lead_err(lead_row_index, message)