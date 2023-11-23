
import streamlit as st
from client import get_response

st.set_page_config(page_title="Rakshita News")

country = st.sidebar.selectbox("Country Name",("India","USA"))
language = st.sidebar.selectbox("Language Name",("English", "Tamil"))
# query = st.text_input("what u need to search?")
# print(query)

data = get_response(country=country,language=language)


st.write("<h1 style='text-align: center;color: red; margin:0; padding:0;'>Rakshita News</h1>", unsafe_allow_html=True)

for i in data:
    
    st.write(f"## {i.title}")
    st.write(", ".join(i.category))

    if i.image_url:
        image = i.image_url
    else:
        with open("assets/default.jpg",'rb') as f:
            image = f.read()
    st.image(image)

    if i.video_url:
        st.write(f'<iframe src={i.video_url}></iframe>')
    else:
        st.write("None")
    st.write(i.description)
    with st.expander("Content"):
        st.write(i.content)
    st.link_button("Read More",i.link)
    st.write(i.pub_date)
    st.divider()
 
