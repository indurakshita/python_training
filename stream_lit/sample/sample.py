import streamlit as st
from PIL import Image

st.title(":red[U.S. News Best Countries]")
st.text("2023 Rankings")
st.write('''The overall ranking of Best Countries measure global performance on a variety of metrics. 
         Switzerland is the best country in the world for 2023.''')

        
col1,col2,col3 = st.columns(3)
with col1:
    image = Image.open("facebook.png")
    st.image(image,width=30)
with col2:
    image = Image.open("twitter.ico")
    st.image(image,width=30)
with col3:
    image = Image.open("us_news.png")
    st.image(image,width=30,use_column_width="auto")

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.button("Rankings")
with col2:
    st.button("Economy")
with col3:
    st.button("Geography")
with col4:
    st.button("Population")
with col5:
    st.button("Sort")





    



