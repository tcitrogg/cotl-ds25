import streamlit as st

st.set_page_config(page_title="Vote | Drama Sunday 25", page_icon="assets/favicon.png")

st.image("assets/voting-site-banner.png")

@st.dialog("You are voting for")
def handle_vote(candidate: str, color: str="white"):
    st.html(f'<h1 style="color: {color}">{candidate}</h1>')
    if st.button("Submit"):
        st.success(f"Voted for {candidate}")
        st.session_state.cotldsvote = {"candidate": candidate}
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
    candidate_name = st.session_state.cotldsvote["candidate"]
    st.title(f"🎊 You voted {st.session_state.cotldsvote['candidate']}")
    image_left, caption_right = st.columns(2)
    with image_left:
        st.image(f"assets/voting-site-{candidate_name.lower()}-avatar.png")
    with caption_right:
        st.write("Support your candidate,\nCopy the caption below and share with loved ones")
        st.code(f"""
🌟 Vote {candidate_name} for President!!!
🔗 https://bit.ly/ds25-vote

#vote #{candidate_name.lower()}4president #cotl #ds25""", language="markdown")
        st.download_button(label="Download",
                           data=open(f"assets/exodus-cand-{candidate_name.lower()}-CAMP.png", mode="rb"),
                           file_name=f"vote_{candidate_name}_for_president.png",
                           mime="image/png"
                           )
    
st.divider()
_, middle, _ = st.columns([0.3, 0.4, 0.15])
with middle:
    st.image("assets/social_mark.png", width=200)