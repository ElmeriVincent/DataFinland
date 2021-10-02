from pandas.io import excel
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
import altair as aa
import plost
import seaborn as sns
from matplotlib import pyplot as plt


#Simple way to display your data, for this we have used population data of Finland.
#I did this while learning about Streamlit.
#Be free to use and customize this code, experiment and try new things.
#- Elmeri Keitaanranta, 17. 


#set_page_config sets a title on your window.
st.set_page_config(page_title="Data Finland", layout="centered",
                                page_icon="images/suomi.png",
                                initial_sidebar_state="expanded")





#heading | quick markdowns...
st.markdown("<h1 style='text-align: center; color: #fff; { font-family: finlandica; } '>Data Finland!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #fff; { font-family: finlandica; } '>Created by Elmeri Keitaanranta</p><br>", unsafe_allow_html=True)
st.markdown("[![Twitter Followers](https://badgen.net/twitter/follow/ElmeriVincent)](https://twitter.com/ElmeriVincent)", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: center; color: #8892B0; { font-family: finlandica; } '>Settings</h1><br>", unsafe_allow_html=True)


#function for viewing population data when clicked certain button on screen.
def choose():
        #Select what will be shown
        total = "Population Growth Finland"
        female = "Females in Finland"
        male = "Males in Finland"
        selection = st.sidebar.radio("Select what chart will be shown.", [total, female, male])



        #TOTAL POPULATION
        if selection == (total):
                '''**Population growth in Finland 2000-2020**'''
                ### --- LOAD DATAFRAME

                excel_file = "data/datapop.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A:B',
                                parse_dates=True)

                plost.area_chart(data, "Year", "Population", height=250, color='#0a81c0')
                plost.pie_chart(data, "Year", "Population", height=250)
                data.set_index('Year', inplace=True)

                #OPTION FOR TOTAL POPULATION
                selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                selected_rows = data.loc[selected_indices]
                st.sidebar.write(selected_rows)


                #Sidebar show raw data
                if st.sidebar.checkbox('Show raw population data'):
                        st.sidebar.subheader('Population Data')
                        st.sidebar.table(data)
                

#_____________________________________________________________________________________________________

        #FEMALES OF TOTAL POPULATION!
        elif selection == (female):

                '''**Female population growth in Finland 2000-2020**'''

                excel_file = "data/datapop.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A,D',
                                parse_dates=True)
                plost.area_chart(data, "Year", "Female", height=250, color='#673ba6')
                

                #OPTION FOR FEMALE POPULATION
                data.set_index("Year", inplace=True)
                selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                selected_rows = data.loc[selected_indices]
                st.sidebar.write(selected_rows)


                #SHOWS RAW DATA OF MALE POPULATION
                if st.sidebar.checkbox('Show raw female population data'):
                        st.sidebar.subheader('Population Data')
                        st.sidebar.table(data)


#_________________________________________________________________________________________________________________

        #MALES OF TOTAL POPULATION!
        elif selection == (male):
                '''**Male population growth in Finland 2000-2020**'''
                excel_file = "data/datapop.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A,C',
                                parse_dates=True)
                plost.area_chart(data, "Year", "Male", height=250, color='#424141')

                #OPTION FOR MALE POPULATION
                data.set_index('Year', inplace=True)
                selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                selected_rows = data.loc[selected_indices]
                st.sidebar.write(selected_rows)


                #SHOWS RAW DATA OF MALE POPULATION
                if st.sidebar.checkbox('Show raw male population data'):
                        st.sidebar.subheader('Population Data')
                        st.sidebar.table(data)

        else:
                '''Error! Please visit the app again soon!'''
choose()




#Audio Anthem
song = "assets/maamme.mp3"
st.sidebar.markdown("<h4 style='text-align: center; color: #8892B0; { font-family: finlandica; } '><br>National Anthem</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #fff; { font-family: finlandica; } '>Maamme (Finnish) || Vårt land (Swedish) || Our land (English)</p>",
unsafe_allow_html=True)
st.sidebar.audio(song)

