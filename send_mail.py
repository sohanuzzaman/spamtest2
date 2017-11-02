from get_mailids import sender_email_ids, all_receiver, get_random, mailid_err, lead_err
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from random import randrange
from ip_handler import reconnect
from smtp_conf import connect_smtp


# defining the initial row indix
lead_row_index = 1

reconnect_init = 0

for item in all_receiver:
    for row in sender_email_ids:
        email_id = row['email_id']
        password = row['password']
        name = row['name']
        occupation = row['occupation']
        vpn_server = row['vpn_server']
        mialid_row_index = row['index']
        # reconnect_init = reconnect(vpn_server, reconnect_init)
        server = connect_smtp(email_id, vpn_server)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # email login
        try:
            server.login(email_id, password)
            # mailid_ip(mialid_row_index, myip)
        except Exception as ex:
            mailid_err(mialid_row_index, ex)
            continue

        #sending email random times from this ID
        sending_time = randrange(10, 15)
        for _ in range(sending_time):

            #updating row index of leaads sheet
            lead_row_index += 1

            try:
                email_receiver = (all_receiver.pop(0))
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
            html = "{0}\n\n{1}\n{2}".format(body, name, occupation)
            msg.attach(MIMEText(html, 'html'))
            try:
                server.sendmail(email_id, email_receiver, msg.as_string())
                lead_err(lead_row_index, "c.sent")
                print("mail sucessfully sent to {}".format(email_receiver))
            except Exception as ex:
                lead_err(lead_row_index, "b.{}".format(ex))
        try:
            server.quit()
        except:
            continue