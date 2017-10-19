from get_mailids import sender_email_ids, all_receiver, final_mail_subject, final_mail_body, mailid_err, lead_err
import smtplib
from random import randrange, shuffle, choice
from ip_handler  import change_ip


# email server credentials

# selecting an gmail smtp server IP hardcoded whitelisted on HMA!pro vpn
def select_smtp_ip():
    available_ips = ["74.125.136.108", "74.125.133.108", "74.125.142.108", "74.125.143.108", "173.194.66.16", "173.194.66.109", "173.194.66.108", "173.194.67.108", "173.194.67.109", "173.194.70.108", "173.194.70.16"]
    shuffle (available_ips)
    server_ip = choice (available_ips)
    return server_ip


# defining the initial row indix
mialid_row_index = 1
lead_row_index = 1

for item in all_receiver:
    for row in sender_email_ids:
        #selecting an smtp server
        smtp_server = select_smtp_ip()
        smtp_port = "465"
        #updating mail ID row index
        mialid_row_index += 1

        email_id = row['email_id']
        password = row['password']
        name = row['name']
        occupation = row['occupation']
        server = row['server']
        #changing IP address to the preferd server
        change_ip(server)

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()  
        server.starttls
        server.ehlo()

        # email login
        try:
            server.login(email_id, password)
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
                #print("mail sucessfully sent to {}".format(email_receiver))
            except Exception as ex:
                lead_err(lead_row_index, "b.{}".format(ex))

        server.quit()

