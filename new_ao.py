import streamlit as st
import pandas as pd
import numpy as pd 
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel("Adidas.xlsx")
print("Hello world ")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)
print(df)
describe(df)
