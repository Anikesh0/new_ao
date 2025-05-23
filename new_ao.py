import streamlit as st
import pandas as pd
import numpy as pd 
from PIL import Image
print("Hello world ")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
if option:
    st.success('This is a success message!', icon="✅")
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
