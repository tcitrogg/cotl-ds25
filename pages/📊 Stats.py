import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Stats | Drama Sunday 25", page_icon="assets/favicon.png")


SheetConn = st.connection("gsheets", type=GSheetsConnection)
stats_data = SheetConn.read(worksheet="ResultPage", usecols=[0, 1], ttl=5)


# st.page_link("app.py", label="Vote", icon="✅")


def get_vote_counts():
    nkuku_count = stats_data["Nkuku"].replace(0.0, np.nan).dropna().count()
    okoli_count = stats_data["Okoli"].replace(0.0, np.nan).dropna().count()
    return int(nkuku_count), int(okoli_count)

st.image("assets/voting-site-banner.png")

st.write(get_vote_counts())

# Data
labels = ['Nkuku', 'Okoli']
values = get_vote_counts()

# Find the highest value
colors = ['blue' if label == "Nkuku" else 'yellow' for label in labels]

# Create a DataFrame
df = pd.DataFrame({'Candidates': labels, 'Votes': values, 'Color': colors})

# Plot the bar chart using Plotly
fig = px.bar(
    df,
    x='Candidates',
    y='Votes',
    color='Color',
    color_discrete_map={'blue': '#1163ad', 'yellow': '#d09715'},
    title="Exodus Campaign",
)

# Customize the chart
fig.update_layout(showlegend=False, yaxis_title="Votes", xaxis_title="Candidates")

# Display the chart in Streamlit
st.plotly_chart(fig)
