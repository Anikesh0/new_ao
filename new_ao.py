import streamlit as st
import pandas as pd
import numpy as pd 
from PIL import Image


df = pd.read_excel("Adidas.xlsx")
print("Hello world ")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)
print(df)
describe(df)
