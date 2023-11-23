import streamlit as st




st.set_page_config(page_title="Online Shopping")
st.write("<h1 style='text-align: center;color: red;'>Online Shopping</h1>", unsafe_allow_html=True)


col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    grocery=st.selectbox(":blue[Grocery]",("oils","snacks"))
    if grocery == "snacks":
        selected_snack = st.selectbox(":green[Snacks Subcategory]", ["All","Biscuits", "Chocolates", "Ice Creams"])
    
with col2:
    st.selectbox(":blue[Mobiles]",["All","One-Plus","OPPO","Realme","Samsung"])
with col3:

    st.selectbox(":blue[Fashion]",("All","Men",'Women_dresses'))
with col4:
    st.selectbox(":blue[Home&Furniture]",("All","Kitchen Tools"))
with col5:
    st.selectbox(":blue[Electonics]",("All","Bluetooth_headphone","charger","headset"))

