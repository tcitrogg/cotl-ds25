import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime
from random import choice as rd_choice

# 
st.set_page_config(page_title="Vote | Drama Sunday 25", page_icon="assets/favicon.png")

SheetConn = st.connection("gsheets", type=GSheetsConnection)
EXISTINGDATA = SheetConn.read(worksheet="ResultPage", ttl=5)


st.image("assets/voting-site-banner.png")

@st.dialog("You are voting for")
def handle_vote(candidate: str, color: str="white"):
    with st.form(key="voting_form"):
        voteid = st.text_input("Phone number*").title()
        st.html(f'<h1 style="color: {color}">{candidate}</h1>')
        submit_button = st.form_submit_button("Confirm Vote")
        if submit_button:
            if not voteid or 15 > len(str(voteid)) < 10:
                st.warning("Invaild Phone Number")
                st.stop()
            else:
                with st.spinner():
                    if candidate == "Nkuku":
                        nkukuScore, okoliScore = (1, 0)
                    else:
                        okoliScore, nkukuScore = (1, 0)
                    timestamp = datetime.now().timestamp()
                    
                    # New Data
                    NEWVOTEDATA = pd.DataFrame([
                        {
                            "Nkuku": nkukuScore,
                            "Okoli": okoliScore,
                            "VoteID": voteid,
                            "Timestamp": timestamp
                        }
                    ])
                    st.session_state.cotldsvote = {"candidate": candidate, "voteid": voteid, "timestamp":timestamp}
                    
                    # Updated Data
                    UPDATED_DATA = pd.concat([EXISTINGDATA, NEWVOTEDATA])
                    
                    # Updated Sheets with updated data
                    SheetConn.update(worksheet="ResultPage", data=UPDATED_DATA)
                    st.toast(f"You Voted {candidate}!!", icon="🎊")
                    st.rerun()

if "cotldsvote" not in st.session_state:
        
    with st.container():
        _, middle, _ = st.columns([0.4, 0.4, 0.15])
        with middle:
            st.title("Vote")
        nkuku_side, okoli_side = st.columns(2)
        with nkuku_side:
            st.image("assets/voting-site-nkuku-avatar.png")
            if st.button("Vote Nkuku"):
                handle_vote("Nkuku", color="#1163ad") # #0b68bb
            
        with okoli_side:
            st.image("assets/voting-site-okoli-avatar.png")
            if st.button("Vote Okoli"):
                handle_vote("Okoli", color="#d09715")
else:
    st.balloons()
    candidate_name = st.session_state.cotldsvote["candidate"]
    st.title(f"🎊 You voted {st.session_state.cotldsvote['candidate']}")
    image_left, caption_right = st.columns(2)
    with image_left:
        st.image(f"assets/voting-site-{candidate_name.lower()}-avatar.png")
    with caption_right:
        st.write(f"Support *{candidate_name}* ✊{rd_choice(['🤩', '😌'])},\nCopy the caption below and share with loved ones")
        st.code(f"""
🌟 Vote {candidate_name} for President!!!
🔗 https://bit.ly/ds25-vote

#vote #{candidate_name.lower()}4president #cotl #ds25""", language="markdown")
        st.download_button(label="Download Campaign Flyer",
                           data=open(f"assets/exodus-cand-{candidate_name.lower()}-CAMP.png", mode="rb"),
                           file_name=f"vote_{candidate_name}_for_president.png",
                           mime="image/png"
                           )
    
st.divider()
_, middle, _ = st.columns([0.3, 0.4, 0.15])
with middle:
    st.image("assets/social_mark.png", width=200)