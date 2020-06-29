import smtplib
from email.message import EmailMessage
import random
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

from other import user_email_id, user_pwd, nums

#The mail addresses and password
sender_address = user_email_id
sender_pass = user_pwd
receiver_address = 'shawnlouis2000@gmail.com'

# generating email OTP
# selects a random number from a list(nums) in other.py file
# this method will be used only for testing purposes
email_otp = random.choice(nums)
content = ("Greetings from SequelString's copy of Practo App!!" + "\n" + "Use this OTP to sign in to your Practo account! Do not Share this code: " + str(email_otp))

msg = EmailMessage()
msg["Subject"] = "OTP Verification For SequelString's Doctor App Login."
msg["From"] = sender_address
msg["To"] = receiver_address
msg.set_content(content)

with smtplib.SMTP(
    "smtp.gmail.com", 587
) as smtp:  # make sure to enable "less secure apps" on google before sending (not recievig) mail , link:https://myaccount.google.com/lesssecureapps
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_address, sender_pass)
    smtp.send_message(msg)
print("Email OTP : ", email_otp)



"""mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')"""