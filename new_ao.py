import streamlit as st
import pandas as pd
from datetime import timedelta, datetime

# Set page config
st.set_page_config(page_title="Anikesh Dashboard", layout="wide")

# Helper functions
@st.cache_data
def load_data():
    data = pd.read_csv("youtube_channel_data.csv")
    data['DATE'] = pd.to_datetime(data['DATE'])
    data['NET_SUBSCRIBERS'] = data['SUBSCRIBERS_GAINED'] - data['SUBSCRIBERS_LOST']
    return data

    

# Load data
df = load_data()

# Set up input widgets







# DataFrame display
with st.expander('See DataFrame (Selected time frame)'):
    st.dataframe(df_filtered)
