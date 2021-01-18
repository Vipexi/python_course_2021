#! /usr/bin/python3

import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders 
# I found that you needed to import many modules, but it was total gibberish to me.

def send_email(subject,body):
    gmail_user = "vipezi13@gmail.com"

    with open("password.txt") as filereader:
        gmail_password = filereader.read()

    #after= datetime.datetime.now()
    #print ("Current date and time : ")
    #print (now.strftime("%Y-%m-%d %H:%M:%S"))
    #return after

    to = ['vipezi13@gmail.com']
    #subject ='error from application'
    #body = after

    msg = EmailMessage ()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to

    while True:
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            
        except:
            print('cannot connect to server')
            break

        try:
            server.login(gmail_user, gmail_password)
            
        except:
            print('error with user name or password')
            break
        
        try:
            server.send_message(msg)
            
        except:
            print('error with sending a mail')
            break
        
        try:
            server.close()

        except:
            print('error with closing server connection')
            break
        break



    #if __name__ == "__main__":
        #send_email("The game has strated", now)