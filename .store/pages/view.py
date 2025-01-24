import streamlit as st
from streamlit_gsheets import GSheetsConnection

SheetConn = st.connection("gsheets", type=GSheetsConnection)

voting_data = SheetConn.read(worksheet="ResultPage")

st.dataframe(voting_data)