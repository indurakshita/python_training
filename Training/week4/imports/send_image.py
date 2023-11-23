"""sending images in email"""

import os
import smtplib
from email.mime.multipart import  MIMEMultipart as add_multipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if not cls in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    

class SendImage:
    os.chdir('../image_folder/')

    def __init__(self,sender_mail,receiver_mail,filename):
            self.sender_mail = sender_mail
            self.receiver_mail = receiver_mail
            self.filename = filename
            self.msg = None
            self.image = None
            
    def image_file_exist(self):  
        try:  
            if os.path.exists(self.filename):
                print("file exist")
                with open(self.filename,"rb") as f:
                    self.image = MIMEImage(f.read())
                    f.close()
                    return self.image
            else:
                print("file not found")
        except Exception as e:
            print(f"{e}")

   
    def add1_multipart(self,body):
        self.msg = add_multipart()
        self.msg["from"] = self.sender_mail
        self.msg["to"] = self.receiver_mail
        self.msg["subject"] = "send the image"
        
        self.msg.attach(MIMEText(body)) #attach the text in body
        if self.image:
            self.msg.attach(self.image)
        return self.msg
    

class SmtpMail(SendImage,metaclass=Singleton):
        def __init__(self,sender_mail,receiver_mail,filename,local_host,port):
            super().__init__(sender_mail,receiver_mail,filename)
            self.local_host = local_host
            self.port = port

        def smtp(self):
            print("sending the mail:")
            password = input("enter the  Email password:")
            try:
                mail = smtplib.SMTP(self.local_host,self.port)
                mail.starttls()
                mail.login(self.sender_mail,password)
                mail.send_message(self.msg)
                print("mail sent successfully")
            except Exception as e:
                print(f"Error is:{e}")

img = SmtpMail(sender_mail="imathi101@gmail.com",receiver_mail="imathi101@gmail.com",
               filename = "nature.jpg",local_host ="smtp.gmail.com",port = 587)
img.image_file_exist()
img.add1_multipart(body="This is the image about nature")
img.smtp()


    