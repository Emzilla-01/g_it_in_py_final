#!/usr/bin/env python3
from email.message import EmailMessage
import smtplib
import mimetypes
import os
from cfg import user, pw

def generate_email(from_="automation@example.com",
                    to =user+"@example.com",
                    subject="Upload Completed - Online Fruit Store",
                    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
                    attachment="/tmp/processed.pdf"):
  m_ = EmailMessage()
  m_['From']=from_
  m_['To']=to
  m_['Subject']=subject
  m_.set_content(body)
  if attachment != None:
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment, 'rb') as att_file:
      m_.add_attachment(att_file.read(),
      maintype=mime_type,
      subtype=mime_subtype,
      filename=os.path.basename(attachment))
  return(m_)

def send_email(m_, sender="automation@example.com", pw=pw):
  server=smtplib.SMTP('localhost',port=25)
  #server.login(sender,pw)
  server.send_message(m_)
  server.quit()


