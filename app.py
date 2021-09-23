from pandas.io import excel
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image
import altair as aa


#set_page_config sets a title on your window.
st.set_page_config(page_title="Data Finland", layout="centered",
                                page_icon="🧊",
                                initial_sidebar_state="expanded")


st.write("![Twitter Follow](https://img.shields.io/twitter/follow/ElmeriVincent?style=social)")


#heading
st.markdown("<h1 style='text-align: center;  { font-family: finlandica; } '>Data Finland!</h1><br>", unsafe_allow_html=True)


'''**Population growth in Finland 1960-2020**'''


def local_css(file_name):
        with open(file_name) as f:
                st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")


### --- LOAD DATAFRAME
excel_file = "data2.xlsx"

data = pd.read_excel(excel_file,
                usecols='A:B',
                parse_dates=True)

data.set_index('Year', inplace=True)

st.line_chart(data)


selected_indices = st.multiselect('Select the Specific year.', data.index)
selected_rows = data.loc[selected_indices]
st.write('### Selected Rows', selected_rows)

#raw data option
if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)