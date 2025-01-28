import streamlit as st

pages = {
    "Campaign": [
        st.Page("route/vote.py", title="Vote your Candidate"),
        st.Page("route/stats.py", title="Campaign Statistics"),
        st.Page("route/support.py", title="Support your Candidate"),
    ],
    "Resources": [
        st.Page("route/learn.py", title="Drama Sunday"),
        # st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages, expanded=True)
pg.run()

st.logo("assets/favicon.png")