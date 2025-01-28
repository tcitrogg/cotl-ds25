import streamlit as st
from random import choice as rd_choice


st.set_page_config(page_title="Support | Drama Sunday 25", page_icon="assets/favicon.png")

def mk_support_page(candidate_name: str):
    image_left, caption_right = st.columns(2)
    with image_left:
        st.image(f"assets/voting-site-{candidate_name.lower()}-avatar.png")
    with caption_right:
        st.subheader(f"Support **{candidate_name}** ✊{rd_choice(['🤩', '😌'])}")
        st.write("Copy the caption below and share with loved ones")
        st.code(f"""
🌟 Vote {candidate_name} for President!!!
🔗 https://bit.ly/ds25-vote

#vote #{candidate_name.lower()}4president #cotl #ds25""", language="markdown")
        st.download_button(label="Download Campaign Flyer",
                           data=open(f"assets/exodus-cand-{candidate_name.lower()}-CAMP.png", mode="rb"),
                           file_name=f"vote_{candidate_name}_for_president.png",
                           mime="image/png", key=f"vote_{candidate_name}"
                           )


NkukuTab, OkoliTab = st.tabs(["Nkuku", "Okoli"])

with NkukuTab:
    mk_support_page("Nkuku")

with OkoliTab:
    mk_support_page("Okoli")