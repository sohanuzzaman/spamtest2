import re


def get_smtp_conf(email_id):
    global smtp_server
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

    print(smtp_server)
    return smtp_server

get_smtp_conf("sosjgoihsgh@hotmail.com")

def connect_smtp(email_id):
    #selecting an smtp server
    smtp_server = get_smtp_conf(email_id)
    smtp_port = "587"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        return server
    except:
        print("failed connecting smtp server :( retrying ...")
        disconnect()
        time.sleep(12)
        connect()
        connect_smtp()