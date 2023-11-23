import os
import datetime as dt
import smtplib
from email.mime.multipart import MIMEMultipart as add_multipart
from email.mime.text import MIMEText

class SendMail:
    def __init__(self,path,sender_mail,receiver_mail):
        self.path = path
        self.sender_mail = sender_mail
        self.receiver_mail = receiver_mail
        self.files = {}
    def get_days_file(self):
        
        for self.file in os.listdir():
            f_create_time = os.path.getctime(self.file)
            file_date = dt.datetime.fromtimestamp(f_create_time).date()
            now = dt.datetime.now().date()
            self.create_days=(now - file_date).days
            if self.create_days >=30:
                self.files[self.file] = self.create_days
        return self.files
                # return f"File or Folder name is: {self.file}\nDays of file creation is :{self.create_days}\n"
    def send_mail(self):
        body = None
        password = input("enter the password:")
        msg = add_multipart()
        msg['From'] = self.sender_mail
        msg['To'] = self.receiver_mail
        msg["Subject"] = "mail for exist file name 30 days ago"
        files = self.files
        if not files:
           return "no files exists in 30 days ago"
        body = f"Files are exists in 30 days ago:\n"
        for file,days in files.items():
            body+= f"File:{file}\nDays:{days}\n"
        msg.attach(MIMEText(body,"plain"))
        
        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.starttls()
            mail.login(self.sender_mail,password)
            mail.send_message(msg)
            print("mail sent successfully")
            mail.quit()

        except smtplib.SMTPAuthenticationError:
            print("password is incorrect")
        except Exception as e:
            print(f"Error is: {e}")

        

send =  SendMail(path=os.chdir('./'),sender_mail="imathi101@gmail.com",receiver_mail="albin.anthony@onedatasoftware.com")
send.get_days_file()
send.send_mail()
    