import streamlit as st
import pandas as pd

'write'
st.write("<h1> Hello </h1>",unsafe_allow_html=True)
st.write("Hello world")
st.title("Hello world",anchor="Indhu")
st.divider()
'markdown'
st.markdown("Hello *world* **world** ***world***")
st.markdown("colors added &mdash;\
             :red[Hello] :blue[world]")
st.markdown("Hello :blue[world] :rose::tulip:")
multi_line = """If you end a line with two spaces,
a soft return is used for the next line.
Two (or more) newline characters in a row will result in a hard return."""
st.markdown(multi_line)
st.divider()
'Text-area'
st.title("Indhu")
md = st.text_area('Hi',
                  "This is Indhu :joy:\n I am python developer")
st.code(f"""
import streamlit as st

# st.markdown({md})
# """)
st.markdown(md)
st.divider()

'Header'

st.header("Hello world",divider='rainbow')
st.header("Hello :blue[world] :rose::tulip:",anchor="Indhu")
st.divider()

'sub header'

st.subheader("This is my Ist website :rose:",divider="blue")
st.divider()
'caption'
st.caption("this is :red[_caption_] :sunglasses: ")
st.divider()
'code'
c="""def func()
    print('Hi,This is Indhu)
func()"""
st.code(c,language="python")
st.divider()
'text'
st.text("This is python",help='code')
st.divider()
'latex'
st.latex('(a+b)^2=a^2+b^2')
st.divider()

'slider'

s_val= st.slider("This is a slider", 0, 100, (25, 75))
st.write(s_val)
print(s_val)
st.divider()

name = st.text_input("enter your name")
if name:
    st.write(f"## Your name is {name}")

st.divider()

img = st.camera_input("Take pic")
if img:
    with open("indhu.jpg",'wb') as f:

        f.write(img.read())





