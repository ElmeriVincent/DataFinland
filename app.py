from pandas.io import excel
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import altair as aa

#set_page_config sets a title on your window.
st.set_page_config(page_title="Data Finland")


#heading
st.markdown("<h1 style='text-align: center;  { font-family: finlandica; } '>Data Finland!</h1><br>", unsafe_allow_html=True)


### --- LOAD DATAFRAME
excel_file = "data.xlsx"

data = pd.read_excel(excel_file,
                usecols='A:B',
                parse_dates=True)

data.set_index('Year', inplace=True)
st.line_chart(data)


#raw data option
if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)