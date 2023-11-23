from streamlit_extras.stodo import to_do 
from streamlit_extras.let_it_rain import rain
import streamlit as st

if not "todos" in st.session_state:
    st.session_state.todos: list = []

def todos():
    st.title("Day of activity")
    
    item = st.text_input("todo")
    if st.button("Add todo"):
        st.session_state.todos.append(item)
        st.experimental_rerun()

    if st.session_state.todos:
        for todo in st.session_state.todos:
            active = st.checkbox(todo, strike_text=True)
            if active:
                # st.session_state.todos.remove(todo)
                st.experimental_rerun()
    

todos()