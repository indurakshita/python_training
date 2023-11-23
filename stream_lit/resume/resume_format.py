import streamlit as st

# def main():
#     r_button = st.sidebar.button("Resume")
#     if r_button:
#         with open("indu_resume.pdf", 'rb') as pdfFileObj:
#             pdf_reader = PdfReader("indu_resume.pdf")
#             pdf_text = ""
#             for page in pdf_reader.pages:
#                 pdf_text += page.extract_text()

#             st.markdown(pdf_text)

# if __name__ == "__main__":
#     main()

# def main():
#     resume_button = st.sidebar.button("Resume")
#     if resume_button:
#         st.title("Resume")

#         with open("res.txt", "r",encoding="utf-8") as file:
#             text = file.read()
#             st.markdown(f"{text}")

# if __name__ == "__main__":
#     main()



# def main():
    
#     resume_button = st.sidebar.button("Resume")
#     if resume_button:
#         st.title("Resume")
#         st.markdown(f"""<html>
# <head>
#     <title>Resume</title>
# </head>
# <body>
#     <h1>INDUMATHI.M</h1>
#     <p>H/O G.Chandramohan<br>
#     120, Mani Nagar,<br>
#     Sivanadhapuram, Saravanampatti,<br>
#     Coimbatore-641035</p>

#     <h2>OBJECTIVE</h2>
#     <p>To obtain an entry into your concern where I can gain some more knowledge and a motive to know more about myself and to establish my sincerity in a correct platform.</p>

#     <h2>EDUCATIONAL PROFILE</h2>
#     <ul>
#         <li>B.E (Electronic and Communications Engineering) – 79% (Apr 2015)
#             <ul>
#                 <li>Christian College of Engineering and Technology, Oddanchatram.</li>
#             </ul>
#         </li>
#         <li>HSC-Tamilnadu Matriculation-89% (Mar 2011)
#             <ul>
#                 <li>Ourlady of Lourdes girl’s higher secondary school, Dindigul.</li>
#             </ul>
#         </li>
#         <li>SSLC-Tamilnadu Matriculation-92% (Apr 2009)
#             <ul>
#                 <li>Sri Vasavi Girl’s High School, Dindigul.</li>
#             </ul>
#         </li>
#     </ul>

#     <h2>TECHNICAL PROFILE</h2>
#     <ul>
#         <li>Platforms: WINDOWS 7, XP, Web Browsers.</li>
#         <li>Packages: MS-Office</li>
#         <li>Computer Language: HTML, CSS, Python.</li>
#         <li>Typist: Both higher (Tamil, English)</li>
#     </ul>

#     <h2>AREA OF INTEREST</h2>
#     <ul>
#         <li>Photoshop</li>
#         <li>Web Designing</li>
#     </ul>

#     <h2>WORK EXPERIENCE</h2>
#     <p>At 2015-2018 I worked at Personiv as a Process Executive in auditing and maintaining the Customer related business details and publishing.</p>

#     <h2>INTERNAL PERSONAL SKILLS</h2>
#     <ul>
#         <li>Known to adapt to changing work environments.</li>
#         <li>Responsible attitude targeted at ensuring completion of projects in a time-efficient manner.</li>
#         <li>Ability to offer sympathy and practice sensitivity in delicate matters.</li>
#         <li>Able to negotiate positively and resolve problems proactively.</li>
#     </ul>

#     <h2>ACHIEVEMENTS</h2>
#     <ul>
#         <li>I received the Shout Out from the Client for the best performance for the year 2017 at Personiv.</li>
#         <li>I was honored with the “Rewards & Recognition” for my progress at Personiv.</li>
#     </ul>

#     <h2>PERSONAL PROFILE</h2>
#     <ul>
#         <li>Date of Birth: 05-07-1994</li>
#         <li>Gender: Female</li>
#         <li>Marital Status: Married</li>
#         <li>Nationality: Indian</li>
#         <li>Language Proficiency: English and Tamil</li>
#     </ul>

#     <h2>DECLARATION</h2>
#     <p>I hereby declare that the above furnished information is true to the best of my knowledge and belief.</p>
# </body>
# </html>
# """,unsafe_allow_html=True)

# if __name__ == "__main__":
#      main()

def resume():
    resume_button = st.sidebar.button("Resume")
    if resume_button:
        st.title("Resume")

    

        st.markdown("INDUMATHI.M<br>H/O G.Chandramohan<br>120, Mani Nagar,<br>Sivanadhapuram, Saravanampatti,<br>Coimbatore-641035", unsafe_allow_html=True)

        st.header("OBJECTIVE")
        st.write("To obtain an entry into your concern where I can gain some more knowledge and a motive to know more about myself and to establish my sincerity in a correct platform.")

        st.header("EDUCATIONAL PROFILE")
        st.markdown("- B.E (Electronic and Communications Engineering) – 79% (Apr 2015)\n  - Christian College of Engineering and Technology, Oddanchatram.")
        st.markdown("- HSC-Tamilnadu Matriculation-89% (Mar 2011)\n  - Ourlady of Lourdes girl’s higher secondary school, Dindigul.")
        st.markdown("- SSLC-Tamilnadu Matriculation-92% (Apr 2009)\n  - Sri Vasavi Girl’s High School, Dindigul.")

        st.header("TECHNICAL PROFILE")
        st.markdown("- Platforms: WINDOWS 7, XP, Web Browsers.")
        st.markdown("- Packages: MS-Office")
        st.markdown("- Computer Language: HTML, CSS, Python.")
        st.markdown("- Typist: Both higher (Tamil, English)")

        st.header("AREA OF INTEREST")
        st.markdown("- Photoshop")
        st.markdown("- Web Designing")

        st.header("WORK EXPERIENCE")
        st.write("At 2015-2018 I worked at Personiv as a Process Executive in auditing and maintaining the Customer related business details and publishing.")

        st.header("INTERNAL PERSONAL SKILLS")
        st.markdown("- Known to adapt to changing work environments.")
        st.markdown("- Responsible attitude targeted at ensuring completion of projects in a time-efficient manner.")
        st.markdown("- Ability to offer sympathy and practice sensitivity in delicate matters.")
        st.markdown("- Able to negotiate positively and resolve problems proactively.")

        st.header("ACHIEVEMENTS")
        st.markdown("- I received the Shout Out from the Client for the best performance for the year 2017 at Personiv.")
        st.markdown("- I was honored with the 'Rewards & Recognition' for my progress at Personiv.")

        st.header("PERSONAL PROFILE")
        st.markdown("- Date of Birth: 05-07-1994")
        st.markdown("- Gender: Female")
        st.markdown("- Marital Status: Married")
        st.markdown("- Nationality: Indian")
        st.markdown("- Language Proficiency: English and Tamil")

        st.header("DECLARATION")
        st.write("I hereby declare that the above furnished information is true to the best of my knowledge and belief.")
