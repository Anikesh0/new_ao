import streamlit as st
import pandas as pd
from datetime import timedelta, datetime
import numpy as np 

# Set page config
st.set_page_config(page_title="abi Dashboard", layout="wide")

# Helper functions
@st.cache_data
def load_data():
    data = pd.read_csv("youtube_channel_data.csv")
    data['DATE'] = pd.to_datetime(data['DATE'])
    data['NET_SUBSCRIBERS'] = data['SUBSCRIBERS_GAINED'] - data['SUBSCRIBERS_LOST']
    return data
    
st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
st.line_chart(df)
    

# Load data
df = load_data()


with st.sidebar:
    st.title(" Anikesh Dashboard")
    st.header("⚙️ Settings")
    
    max_date = df['DATE'].max().date()
    min_date = df['DATE'].min().date()
    default_start_date = min_date
    default_end_date = max_date
    start_date = st.date_input("Start date", default_start_date, min_value=df['DATE'].min().date(), max_value=max_date)
    end_date = st.date_input("End date", default_end_date, min_value=df['DATE'].min().date(), max_value=max_date)
    time_frame = st.selectbox("Select time frame",
                              ("Daily", "Weekly", "Monthly", "Quarterly"),
    )
    chart_selection = st.selectbox("Select a chart type",
                                   ("Bar","Pie chart","Line chart","Area"))
