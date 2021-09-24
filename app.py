from pandas.io import excel
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
import altair as aa
import plost

#Simple way to display your data, for this we have used population data of Finland.
#I did this while learning about Streamlit. The code is nothing special, it's a simple layout.
#Be free to use and customize this code, expreriment and try new things.
#- Elmeri Keitaanranta, 17. 


#set_page_config sets a title on your window.
st.set_page_config(page_title="Data Finland", layout="centered",
                                initial_sidebar_state="expanded")




#heading
st.markdown("<h1 style='text-align: center;  { font-family: finlandica; } '>Data Finland!</h1><br>", unsafe_allow_html=True)


'''**Population growth in Finland 1960-2020**'''


### --- LOAD DATAFRAME
excel_file = "data2.xlsx"

data = pd.read_excel(excel_file,
                usecols='A:B',
                parse_dates=True)

plost.line_chart(data, "Year", "Population")
data.set_index('Year', inplace=True)

#user can select specific year and show it's population.
selected_indices = st.multiselect('Select the Specific year.', data.index)
selected_rows = data.loc[selected_indices]
st.write('### Result', selected_rows)


#raw data option
if st.sidebar.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)

#Twitter, Change the ElmeriVincent to your own twitter name.
st.write("![Twitter Follow](https://img.shields.io/twitter/follow/ElmeriVincent?style=social)")
