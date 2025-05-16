import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    select=option_menu(
        menu_title="Vinsup Infotech",
        options=["Intenship","About","Contact"],
        icons=['book','file-person','telephone']
    )
if select=="Intenship":
    st.title("Intenship Application")
    st.text_input("Name")
    st.text_input("College Name")
    st.selectbox("Department",["CSE","ECE","IT","AIDS"])
    st.selectbox("Gender",["Male","Female"])
    st.selectbox("course",["Python full stack","Java full stack","C,C++,Python","C,C++,Java","Machine Learning"])
    st.button("Submit")
elif select=="About":
    st.title("Vinsup Infotech")
    st.write("Vinsup Infotech Private Limited is a dynamic Indian IT company specializing in software development, digital solutions, and IT training. Established on March 16, 2022, the company is headquartered in Kadayanallur, Tirunelveli, Tamil Nadu. It is registered under the Corporate Identification Number (CIN)")
    st.write("## Training and Placement")
    st.write(" Operating as a software training and development center, Vinsup Infotech offers programs for both freshers and professionals aiming to advance their careers. The training is conducted by industry experts with over 20 years of experience .")
    st.balloons()
elif select=="Contact":
    st.title("Contact Details")
    st.write("## Madurai Branch")
    st.write("Address: 1st Floor, P.M. Tower, Kalavasal Signal, Madurai, Tamil Nadu 625016 ")
    st.write("## Phone Numbers")
    st.write("General Inquiries: +91 7395 956 587 ")
    st.write(" Training & Placement: +91 94896 49696")
    st.write("## Email")
    st.write("General Inquiries: info@vinsupinfotech.com")
    st.write("Support: support@vinsupinfotech.com")
    st.write("Madurai Branch: vinsupinfotech.madurai@gmail.com")
   