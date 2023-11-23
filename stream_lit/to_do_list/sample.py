import streamlit as st


def add_todo():
    add_sch = {}
    st.header("add todo list")
    col1,col2 = st.columns(2)
    with col1:
        add = st.text_input("add schedule")

    with col2:
        date= st.date_input("Due date")
    if st.button("submit"):
        st.success("Add successfully")
        add_sch[add] = date
        st.write(add_sch)
def read_todo():
    
        st.header("Read todo list")
        add = add_todo()
        st.write(add)


def update_todo():
    st.header("Update todo list")
    add_todo()

def delete_todo():
    st.header("delete todo list")






def main():
    st.sidebar.title("To Do list")


    option = st.sidebar.selectbox('Menu',("Add",'Read',"Update","Delete"))
    if option == "Add":
        add_todo()
    elif option == "Read":
        read_todo()
    elif option == "Update":
        update_todo()
    elif option == "Delete":
        delete_todo()

if __name__ == "__main__":
    main()