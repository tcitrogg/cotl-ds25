import streamlit as st

st.set_page_config(page_title="Learn | Drama Sunday 25", page_icon="assets/favicon.png")

st.video("https://youtu.be/rXM6IxCHZX8")

st.header("Exodus")

st.write("""
- on Sunday, 2nd Feb, 2025
- by 10AM
- at Chapel Of The Light, Main Campus Unilorin
""")


st.divider()
_, middle, _ = st.columns([0.3, 0.4, 0.15])
with middle:
    st.link_button(label="@chapelunilorin", url="https://zaap.bio/Chapelunilorin")
    st.image("assets/social_mark.png", width=200)