import streamlit as st
from readmail import read_mail
from sendmail import SmtpMail
import imaplib 
st.set_page_config("Email")

if not "smtp_obj" in st.session_state:
    st.session_state["smtp_obj"] = None

if not "imap_obj" in st.session_state:
    st.session_state["imap_obj"] = None

def send(mail):
    rec_mail = st.text_input("Receiver Email Address", placeholder="receiveremail@example.com", key="rec_mail")
    subject = st.text_input("Subject", key="subject")
    body = st.text_input("Body", key="body")
    send_button = st.button("submit")

    if rec_mail and subject and body:
        if send_button:
            try:
                mail.send_mail(rec_mail, subject, body)
                st.sucess("Email has been sent successfully!")          
            except:
                st.error("Failed to send the email. Please check your inputs and credentials.")

def login():
     email = st.text_input("Enter your email")
     password = st.text_input("Enter your password")
     if st.button("Login"):
        smtp = SmtpMail(email,password)
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email, password)
        st.success("logged in successfully")
        return smtp, imap
    
def read(imap_obj):
    messages = read_mail(imap_obj)
    
    for msg in messages:
        st.header(msg.subject)
        st.write(msg.from_)
        st.write(msg.body)
        st.divider()


def main():
    st.sidebar.title(":blue[Gmail login App]")
    choice = st.sidebar.selectbox(":red[Menu]",["Login", "Send Mail","Read Mail"])
    if choice == "Login":
        if not st.session_state.smtp_obj and not st.session_state.imap_obj:
            mets = login()
            if isinstance(mets, tuple):
                st.session_state.smtp_obj, st.session_state.imap_obj = mets
        else:
            st.write("You are already logged in")
            if st.button("Logout"):
                st.session_state.smtp_obj = None
                st.experimental_rerun()

    elif choice == "Send Mail":
        if st.session_state.smtp_obj:
            send(st.session_state.smtp_obj)
        else:
            st.error("Login Required!!")
    elif choice == "Read Mail":
        if st.session_state.imap_obj:
            read(st.session_state.imap_obj)
        else:
            st.error("Login Required!!")
if __name__ == "__main__":
    main()
