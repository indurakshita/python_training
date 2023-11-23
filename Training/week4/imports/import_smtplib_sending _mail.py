"method 1"
# import smtplib

# msg = smtplib.SMTP("smtp.gmail.com", 587)
# msg.starttls()
# password = input("Enter your Gmail password: ")
# msg.login("imathi101@gmail.com",password)
# subject = "Test mail from python"
# message = f"Subject:{subject}\nHai This is Indhu\n I completed my mail task"
# msg.sendmail("imathi101@gmail.com","chandrucm195@gmail.com",message)
# print("mail has been sent")
# msg.quit()


'method 2:'
# import smtplib
# import email.message

# print("sending the mail:")
# password = input("enter the  Email password:")
# message = email.message.EmailMessage()
# message["From"] = "imathi101@gmail.com"
# message["To"] = "chandrucm195@gmail.com"
# message["Subject"] = "Test mail from python"
# message.set_content= "Hai I am Indhu\n I am Python Developer"

# msg = smtplib.SMTP("smtp.gmail.com", 587)
# msg.starttls()

# msg.login("imathi101@gmail.com",password)
# msg.send_message(message)
# print("mail has been sent")
# msg.quit()

# ----------------------------------------------------------------------------
# 'logic 2'

# import smtplib
# import email.message


# print("sending the mail:")
# password = input("enter the  Email password:")

# message = email.message.EmailMessage()
# message["From"] = "imathi101@gmail.com"
# message["To"] = "chandrucm195@gmail.com"
# message["Subject"] = "Test mail from python"
# message.set_content= "Hai I am Indhu\n I am Python Developer"


# try: 
#     with smtplib.SMTP("smtp.gmail.com",587) as server:
#         server.starttls()
#         server.login("imathi101@gmail.com",password)
#         server.send_message(message)
#         print("Email has sent successfully")
        
# except smtplib.SMTPAuthenticationError:
#     print("password is incorrect")
# except Exception as e:
#     print(f"Error:{e}")

# ---------------------------------------------------------------------------------
