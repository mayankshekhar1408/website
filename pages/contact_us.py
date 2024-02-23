import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="email_form"):
    user_email=st.text_input("Your Email message")
    option=st.selectbox("Whattopic do you want to discuss?",
                    ('Project Proposal','Job Enquiries','Other'))
    message_box=st.text_area("Your message")
    message=f"""\
Subject: Python App development

From: {user_email}
topic: {option}
{message_box}

"""
    button=st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email has been sent successfully")