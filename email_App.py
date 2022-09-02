import email
from email.message import EmailMessage
from app import password
from app import mail
import smtplib
import ssl

email_sender=mail
email_password=password

email_recevier=''

subject="Python"

body="""
Successfull!!
"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_recevier
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_recevier,em.as_string())

