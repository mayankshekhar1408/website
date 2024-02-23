import smtplib
import ssl
import os

def send_email(message):
    host="smtp.gmail.com"
    port=465
    context=ssl.create_default_context()

    username="mayankshekhar1408@gmail.com"
    password="xxx"

    receiver="smartestmayankk@gmail.com"

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
