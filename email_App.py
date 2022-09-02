import email
from email.message import EmailMessage

import smtplib
import ssl

email_sender='canseverbeyzanur.01@gmail.com'
email_password='qrumwaidatmtifjn'

email_recevier='xoxexi8286@xitudy.com'

subject="i am sending mail through code"

body="""
When you saw this that is mean i successed it
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

