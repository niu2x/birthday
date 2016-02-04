# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def send_mail(mailFrom, rcpt, subject, content):
        message = MIMEText(content, 'utf8')
        message['Content-Type']='text/html;charset=utf-8'
        message['subject'] = subject
        message['From'] = mailFrom
        message['To'] = rcpt
        server = smtplib.SMTP('127.0.0.1')
        server.sendmail(mailFrom, rcptToList, message.as_string())
        server.quit()
