import re, smtplib, time
from ip_handler import reconnect, disconnect
from random import choice, shuffle



def get_smtp_conf(email_id):
    s = re.findall(".*(?<=\@)(.*?)(?=\.)", "From: {}".format(email_id))
    domain = s[0]
    if domain == "gmail":
        smtp_server = "smtp.gmail.com"
    elif domain == "yahoo" or domain == "ymail" or domain == "rocketmail":
        smtp_server = "smtp.mail.yahoo.com"
    elif domain == "outlook" or domain == "hotmail" or domain == "live" or domain == "aol":
        smtp_server = "smtp-mail.outlook.com"
    else:
        print("email address is not recognised py smtp detector")

    print("Detected SMTP server is {}".format(smtp_server))
    return smtp_server


def connect_smtp(email_id, vpn_server):
    #selecting an smtp server
    smtp_server = get_smtp_conf(email_id)
    smtp_port = "465"
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    except:
        print("failed connecting smtp server :( retrying ...")
        # reconnect(vpn_server, 0)
        time.sleep(10)
        connect_smtp(email_id)
    return server
