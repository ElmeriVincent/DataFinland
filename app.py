from pandas.io import excel
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
import altair as aa
import plost
import seaborn as sns

#Simple way to display your data, for this we have used population data of Finland.
#I did this while learning about Streamlit. The code is nothing special, it's a simple layout.
#Be free to use and customize this code, expreriment and try new things.
#- Elmeri Keitaanranta, 17. 


#set_page_config sets a title on your window.
st.set_page_config(page_title="Data Finland", layout="centered",
                                page_icon="assets/suomi.png",
                                initial_sidebar_state="expanded")





#heading
st.markdown("<h1 style='text-align: center; color: #fff; { font-family: finlandica; } '>Data Finland!</h1><br>", unsafe_allow_html=True)


st.markdown("[![Twitter Followers](https://badgen.net/twitter/follow/ElmeriVincent)](https://twitter.com/ElmeriVincent)", unsafe_allow_html=True)


st.sidebar.markdown("<h1 style='text-align: center; color: #0a81c0; { font-family: finlandica; } '>Settings</h1><br>", unsafe_allow_html=True)



def choose():
        #Select what will be shown
        total = "Population Growth Finland"
        female = "Females in Finland"
        male = "Males in Finland"
        selection = st.sidebar.radio("Select what will be shown to chart", [total, female, male])


        #Total population
        if selection == (total):
                '''**Population growth in Finland 2000-2020**'''
                ### --- LOAD DATAFRAME

                excel_file = "assets/PoP.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A:B',
                                parse_dates=True)

                plost.area_chart(data, "Year", "Population", height=250, color='#0a81c0')
                data.set_index('Year', inplace=True)

                #user can select specific year and show it's population.
                selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                selected_rows = data.loc[selected_indices]
                st.sidebar.write(selected_rows)

#_____________________________________________________________________________________________________

        #Females of Total population
        elif selection == (female):

                '''**Females in Finland 2000-2020**'''

                excel_file = "assets/PoPf.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A:B',
                                parse_dates=True)

                plost.area_chart(data, "Year", "Female", height=250, color='#7f0045')


                data.set_index('Year', inplace=True)
                selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                selected_rows = data.loc[selected_indices]
                st.sidebar.write(selected_rows)


        #Males of Total population
        elif selection == (male):
                '''**Males in Finland 2000-2020**'''
                excel_file = "assets/PoPm.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A:B',
                                parse_dates=True)

                plost.area_chart(data, "Year", "Male", height=250, color='#424141')
                data.set_index('Year', inplace=True)
                selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                selected_rows = data.loc[selected_indices]
                st.sidebar.write(selected_rows)

        else:
                '''Error! Please visit the app again soon!'''
choose()



#Sidebar show raw data
        #if st.sidebar.checkbox('Show raw population data'):
                #st.sidebar.subheader('Population Data')
                #st.sidebar.table(data)







