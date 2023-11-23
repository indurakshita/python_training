import os
from smtplib import SMTP
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from Auto_Email.bot.utils.env import MESSAGE, EMAIL, PASSWORD, PERSONAL

base_dir = os.path.dirname(__file__)

def compile(from_, to, subj=None, body=None, docs=None):
    """ Script for compiling email """
    print("Compiling Email...")
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = to
    msg['Subject'] = subj if subj else "Sample Subject"
    messages = body if body else "Sample Body"
    msg.attach(MIMEText(messages, 'plain'))
    
    if docs:
        for filename in docs:
            with open(f"{base_dir}/docs/{filename}", "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                  
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            msg.attach(part)
    return msg.as_string()
    
def send_mail(email=EMAIL, to=None, msg=None) -> None:
    """ Script for sending email using gmail imap server"""
    SERVER = "smtp.gmail.com"
    PORT = 587
    
    with SMTP(SERVER, PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL, PASSWORD)
        print("Logged In Successfully")
        print("Sending Email...")
        smtp.sendmail(EMAIL, to, msg)
        print("Email Successfully Sent!")
    return True

def send(compData):
    print("Preparing Email Data...")
    subj = f"Job application for {compData.position}"
    
    
    docs = {"cv/docs": list(os.listdir(os.path.dirname(__file__)+"/docs/"))}
    doc_str = "\n" + "\n".join([f"{idx}. {i.title()}" for idx, i in enumerate(docs, start=1)])
    body = MESSAGE.format(email=EMAIL, docs=doc_str, **PERSONAL , **compData.dict())
    msg = compile(EMAIL, compData.to, subj=subj, body=body, docs=docs["cv/docs"])
    return send_mail(to=compData.to, msg=msg)
        
s=send()
print(s.body)


