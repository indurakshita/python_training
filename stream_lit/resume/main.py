
import streamlit as st
import sys
import time
from resume_format import resume
from streamlit_extras import add_vertical_space as avs 

st.set_page_config("Indu Resume")

def home():
    home_button = st.sidebar.button("Home")
    if home_button:
        avs.add_vertical_space(10)
        st.title("M.Indumathi")
        st.write("I am Developer")
        
            
def about():
    about_button = st.sidebar.button("About")
    if about_button:
        st.title("About")
        text = """To obtain an entry into your concern where I can gain some more knowledge 
                 and a motive to know more about myself and to establish my sincerity in a correct platform."""
        st.write(text)
        col1, col2 = st.columns(2)
        with col1:
            st.header("image")
        with col2:
            st.header(":blue[**Python Developer**]")
            st.write("**DOB** : 05-07-1994")
            st.write("**Age** : 29")
            st.write("**Degree** : B.E")
            st.write("**Phone no** : +91 78455-03689")
            st.write("**Email id** : imathi101@gmail.com")
            st.write("**City** : Coimbatore")
home()
about()
resume()