import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import requests
import json
from PIL import Image

st.set_page_config(page_title="Data Finland")
st.markdown("<h1 style='text-align: center;'>Data Finland!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: left;'>This is a small data app about Finland,which include roadaccidents, population, most populated areas, etc...</p>", unsafe_allow_html=True)




### --- LOAD DATAFRAME
excel_file = 'data.xlsx'

df = pd.read_excel(excel_file,
                    usecols='A:B',
                    header=0)

st.dataframe(df)

