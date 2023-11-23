import streamlit as st
from streamlit_extras import add_vertical_space as avs 
from client import get_response


st.set_page_config(
    page_title="Weather",
    page_icon=":sunny:",
    layout="wide",
    initial_sidebar_state="expanded"
)

css = """
<style>
body {
    background-color: red; /* Replace with your desired background color */
}
</style>
"""

# Display the CSS
st.markdown(css, unsafe_allow_html=True)



st.header(":blue[Today]")

place= st.sidebar.text_input(":blue[**Place**]",'Coimbatore')
data=get_response(place)

def sidebar():
    st.sidebar.image("weather.png")

    def cloud(temp=None):
        if temp >=30:
            with st.sidebar:
                st.markdown(f'<p style="text-align: center; color: blue">{temp}°C<br>Partly Cloudy</p>',
                            unsafe_allow_html=True)
                st.divider()
                 
        elif temp >=60:
            with st.sidebar:
                st.markdown(f'<p style="text-align: center; color: blue">{temp}°C<br>Partly Sunny</p>',
                            unsafe_allow_html=True)
                st.divider()
                
        elif temp>=70:
            with st.sidebar:
                st.markdown(f'<p style="text-align: center; color: blue">{temp}°C<br>Mostly Cloudy</p>',
                            unsafe_allow_html=True)
                st.sidebar.divider()
                
        elif temp>=90:
            with st.sidebar:
                st.markdown(f'<p style="text-align: center; color: blue">{temp}°C<br>Over Cast</p>',
                            unsafe_allow_html=True)
                st.divider()
                
        st.divider()
    cloud(temp=data.temp_c)


    formatted_date = data.last_updated.strftime('%d-%b-%Y\n%A%I:%M%p')
    st.sidebar.markdown(f'<p style="text-align: center; color: blue">{formatted_date}</p>',unsafe_allow_html=True) 
    avs.add_vertical_space(1)
    st.sidebar.markdown(f'<p style="text-align: center; color: blue">{data.location.region}</p>',
                        unsafe_allow_html=True)
    avs.add_vertical_space(1)
    st.sidebar.markdown(f'<p style="text-align: center; color: blue">{data.location.country}</p>',
                        unsafe_allow_html=True)
    avs.add_vertical_space(1)
    
def main_page():
    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric("lat",data.location.lat)
    with col2:
        st.metric("lon",data.location.lon)
    with col3:
        st.metric("wind",data.wind_kph,'kph')

    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric("Celsius",data.temp_c)
    with col2:
        st.metric("Fahrenheit",data.temp_f)
    with col3:
        st.metric("wind",data.wind_dir,"dir")

sidebar()
main_page()






