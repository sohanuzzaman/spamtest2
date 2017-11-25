from get_mailids import sender_email_ids, all_receiver, get_random, mailid_err, lead_err
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from random import randrange
from ip_handler import reconnect
from smtp_conf import get_smtp_conf


# defining the initial row indix
lead_row_index = 1

def get_bcc_lead():
    global lead_row_index
    bcc_mail = []
    count = randrange(10, 20)
    lead_row_index += count
    for _ in range(count):
        try:
            lead = (all_receiver.pop(0))
            bcc_mail.append(lead)
        except:
            pass
    # recevers = ", ".join(bcc_mail)
    # print(recevers)
    return bcc_mail

for item in all_receiver:
    for row in sender_email_ids:
        email_id = row['email_id']
        password = row['password']
        name = row['name']
        occupation = row['occupation']
        mialid_row_index = row['index']
        vpn_server = row['vpn_server']

        # Connecting to vpn
        reconnect(vpn_server)

        # Connecting to SMTP
        try:
            smtp_server = get_smtp_conf(email_id)
            smtp_port = "587"
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email_id, password)
            # mailid_ip(mialid_row_index, myip)
        except Exception as ex:
            mailid_err(mialid_row_index, ex)
            continue

        #sending email random times from this ID
        sending_time = randrange(2, 4)
        for _ in range(sending_time):

            #updating row index of leaads sheet
            lead_row_index += 1

            try:
                email_receiver = (all_receiver.pop(0))
                bcc_recevers = get_bcc_lead()
            except:
                print ("there is no leads to send")
                break
            subject = get_random("subject")
            body = get_random("body")
            # message = """From: {0}\nTo: {1}\nSubject: {2}\n\n{3}\n\n{4}\n{5}
            # """.format(email_id, email_receiver, subject, body, name, occupation)
            msg = MIMEMultipart('alternative')
            msg['From'] = formataddr((str(Header(name)), email_id))
            msg['To'] = email_receiver
            msg['Subject'] = subject
            body_text = "{0}\n\n{1}\n{2}".format(body, name, occupation)
            msg.attach(MIMEText(body_text))
            try:
                server.sendmail(email_id, [email_receiver] + bcc_recevers, str(msg))
                lead_err(lead_row_index, "c.sent")
                print("mail sucessfully sent to {}".format(email_receiver))
                print(*bcc_recevers, sep='\n')
            except Exception as ex:
                lead_err(lead_row_index, "b.{}".format(ex))
                break
        try:
            server.quit()
        except:
            pass