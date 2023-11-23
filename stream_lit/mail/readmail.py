import email
from pydantic import BaseModel


class Message(BaseModel):
    from_: str
    to: str
    subject: str
    body: str



def read_mail(mail, folder="inbox"):
    mail.select(folder)
    
    _, message_numbers = mail.search(None, "ALL")
    message_numbers = message_numbers[0].decode("utf-8").split()
    message_numbers = reversed(message_numbers)
    for num in message_numbers:
        status, msg_data = mail.fetch(num, "(RFC822)")
        
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)
        from_ = msg['From']
        to = msg["To"]
        subject = msg['subject'] 
        body = ""
        for i in msg.walk():
            if str(i.get_content_type()) == "text/plain":
                body += str(email.message_from_string(i.get_payload())) + "\n"
        
        message = Message(
            from_=from_,
            to=to,
            subject=subject,
            body=body
        )
        yield message
         
    
    mail.close()


if __name__ == "__main__":
    emails = read_mail("imathi101@gmail.com", "phinocmtdmsrlukc")

    for e in emails:
        print(e)
        print("\n\n")






 
    


    
    
    

