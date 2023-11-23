from smtplib import SMTP, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class SmtpMail:
    def __init__(self,sender_mail, password):
            self.sender_mail = sender_mail
            self.password = password
            self.msg = None

    def __client(self):
        try:
            mail = SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.ehlo()
            mail.login(self.sender_mail,self.password)
            return mail
        
        except SMTPAuthenticationError as smtp_error:
            print(f"Error is:{smtp_error}")
            

    def __body_mail(self, to, subject, body, image=None):
        self.msg = MIMEMultipart()
        self.msg["from"] = self.sender_mail
        self.msg["to"] = to
        self.msg["subject"] = subject
        if body:
            self.msg.attach(MIMEText(body))
        if image:
            self.msg.attach(MIMEImage(image))
        return self.msg.as_string()
        
    def send_mail(self, to, subject, body, image=None):
        mail = self.__client()
        email_body = self.__body_mail(to, subject, body, image)
        mail.sendmail(from_addr=self.sender_mail, to_addrs=to, msg=email_body)
        



if __name__ == "__main__":
    mail = SmtpMail("imathi101@gmail.com","phinocmtdmsrlukc")
    mail.send_mail("imathi101@gmail.com", "Hello world", "This is an automated mail from python")
            



