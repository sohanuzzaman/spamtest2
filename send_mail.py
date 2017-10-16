from get_mailids import sender_email_ids, all_receiver, final_mail_subject, final_mail_body, mailid_err, lead_err
import smtplib
from random import randrange



# email server credentials
smtp_server = "smtp.gmail.com"
smtp_port = "587"

# defining the initial row indix
mialid_row_index = 1
lead_row_index = 1

for item in all_receiver:
    for row in sender_email_ids:
        #updating mail ID row index
        mialid_row_index += 1

        email_id = row['email_id']
        password = row['password']
        name = row['name']
        occupation = row['occupation']

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()

        # email login
        try:
            server.login(email_id, password)
        except:
            mailid_err(mialid_row_index)
            continue

        #sending email random times from this ID
        sending_time = randrange(16,23)
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
                print("mail sucessfully sent to {}".format(email_receiver))
            except Exception as ex:
                lead_err(lead_row_index, "failed to send email via SMTP Err message {}".format(ex))

        server.quit()

