# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 00:11:30 2020

@author: tejaswi
Python 3.7
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#https://myaccount.google.com/lesssecureapps,Go to the link with the email you want to send the bulk mails and enable the option.

fromaddr = 'YOUR EMAIL FROM WHICH YOU HAVE TO SEND THE MAIL'
toaddr = ['xyz@gmail.com','abc@gmail.com'] #list of recipients you have to send the mail.
msg = MIMEMultipart()
body = "BODY" #message body
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Your Password")
text = msg.as_string()
for i in toaddr:
    msg['From'] = fromaddr
    msg['To'] = i
    msg['Subject'] = "SUBJECT" #subject
    server.sendmail(fromaddr, i, text)
    print("mail successfully sent to "+i)
server.quit()



