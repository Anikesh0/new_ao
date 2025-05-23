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

