import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# 
st.set_page_config(page_title="Feedback | Drama Sunday'25", page_icon="assets/favicon.png")

# 
SheetConn = st.connection("gsheets", type=GSheetsConnection)
EXISTINGDATA = SheetConn.read(worksheet="Feedback", ttl=5)

def handle_feedback():
    with st.form(key="feedback_form"):
        feedback = st.text_area(label="Tell us your experience at Exodus?")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            with st.spinner():
                NEWFEEDBACKDATA = pd.DataFrame([{
                    "Feedback": feedback,
                    "Timestamp": datetime.now().timestamp()
                }])
                UPDATED_DATA = pd.concat([EXISTINGDATA, NEWFEEDBACKDATA])
                
                # Updated Sheets with updated data
                SheetConn.update(worksheet="Feedback", data=UPDATED_DATA)
            st.toast(f"Thank you for the feedback", icon="🙏")
            

st.header("Your Experience at Exodus?")
handle_feedback()

st.image("assets/exodus-thank_you.jpg")