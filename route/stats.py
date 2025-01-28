import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Stats | Drama Sunday 25", page_icon="assets/favicon.png")


SheetConn = st.connection("gsheets", type=GSheetsConnection)
stats_data = SheetConn.read(worksheet="ResultPage", usecols=[0, 1, 4], ttl=5)


# st.page_link("app.py", label="Vote", icon="✅")
totalvotes_count = stats_data["Flag"].count()
vaildvotes_count = stats_data["Flag"].replace(0.0, np.nan).dropna().count()

vaildstats_data = stats_data[stats_data["Flag"] != 0.0]

def get_vote_counts():
    nkuku_count = vaildstats_data["Nkuku"].replace(0.0, np.nan).dropna().count()
    okoli_count = vaildstats_data["Okoli"].replace(0.0, np.nan).dropna().count()
    return int(nkuku_count), int(okoli_count)

st.image("assets/voting-site-banner.png")

# Data
labels = ['Nkuku', 'Okoli', "Invaild Votes"]
values = [*get_vote_counts(), totalvotes_count - vaildvotes_count]
nkuku_count, okoli_count, invaildvotes_count = values

# Find the highest value
# colors = ['blue' if label == "Nkuku" else 'yellow' for label in labels]
colors = ["blue", "yellow", "red"]

# Create a DataFrame
df = pd.DataFrame({'Candidates': labels, 'Votes': values, 'Color': colors})

# Plot the bar chart using Plotly
fig = px.bar(
    df,
    x='Candidates',
    y='Votes',
    color='Color',
    color_discrete_map={'blue': '#1163ad', 'yellow': '#d09715', "red": "crimson"},
    title="Exodus Campaign",
)

# Customize the chart
fig.update_layout(showlegend=False, yaxis_title="Votes", xaxis_title="Candidates")

# Display the chart in Streamlit
st.plotly_chart(fig)

nkuku_count, okoli_count = get_vote_counts()
icon_side, left_side, middle_side, right_side = st.columns([0.1, 0.3, 0.3, 0.3], vertical_alignment="center")

with icon_side:
    st.html(f'<span style="font-size: 1.75rem; font-weight: bold;">📊</span>')
with left_side:
    st.html(f'<span style="color: #1163ad; font-size: 1.75rem; font-weight: bold;">Nkuku: {nkuku_count}</span>')
with middle_side:
    st.html(f'<span style="color: #d09715; font-size: 1.75rem; font-weight: bold;">Okoli: {okoli_count}</span>')
with right_side:
    st.html(f'<span style="color: crimson; font-size: 1.75rem; font-weight: bold;">Invaild: {invaildvotes_count}</span>')

st.header(f":green[Total votes: {totalvotes_count}]")

st.header(f"{invaildvotes_count} votes were flagged invaild!", anchor="InvaildVotesReport")
zinec_warning = """
**ZINEC Flags Invalid Votes to Ensure Fair Elections**  

The Z Islands National Electoral Committee (ZINEC) has identified and flagged certain inappropriate votes as **invalid**. In a statement, ZINEC emphasized the importance of citizens supporting their preferred candidates with honesty to maintain the integrity of the electoral process.  

The committee assured the public of its commitment to fairness, adding that any attempt to manipulate results through inappropriate VoteIDs _voters phone numbers_ will be flagged and addressed.  

ZINEC encourages all citizens to uphold the principles of fair participation as the election process continues.  

*Signed,*  
**ZINEC Committee**
"""
st.write(zinec_warning)


# the first i wrote, before paraphrasing with chatgpt
# Z Islands National Electoral Commitee (ZINEC) detected some inappropriate votes and they have been flagged as **Invaild**, citizens should support their candidate with all honesty and we ensure this election continue to remain fair, and we will flag inappropriate VoteID _also known as phone numbers_ that are attempting to manipulate the results.
         
# Signed
# ZINEC Commitee