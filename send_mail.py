from get_mailids import sender_email_ids, all_receiver, final_mail_subject, final_mail_body, mailid_err, mailid_ip, lead_err
import smtplib
from random import randrange, shuffle, choice
from ip_handler import connect, disconnect
from smtp_conf import connect_smtp


# defining the initial row indix
mialid_row_index = 1
lead_row_index = 1

for item in all_receiver:
    for row in sender_email_ids:
        #connect to the internet in order to get assigned with a new IP
        connect()
        mialid_row_index += 1
        email_id = row['email_id']
        password = row['password']
        name = row['name']
        occupation = row['occupation']
        #changing IP address to the preferd server
        #myip = change_ip()
        # print("initiling openvpn")
        server = connect_smtp(email_id)
        server.ehlo()
        server.starttls(keyfile=None, certfile=None, context=None)
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

            message = """From: {0}\nTo: {1}\nSubject: {2}\n\n{3}\n\n{4}\n{5}
            """.format(email_id, email_receiver, final_mail_subject, final_mail_body, name, occupation)

            try:
                server.sendmail(email_id, email_receiver, message)
                lead_err(lead_row_index, "c.sent")
                print("mail sucessfully sent to {}".format(email_receiver))
            except Exception as ex:
                lead_err(lead_row_index, "b.{}".format(ex))

        server.quit()
        #disconnect the internet in order to get a new IP
        disconnect()