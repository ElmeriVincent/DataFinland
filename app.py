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
from streamlit.commands.page_config import set_page_config
import streamlit.components.v1 as components
import csv


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
st.sidebar.markdown("<h1 style='text-align: center; color: #8892B0; { font-family: finlandica; } '>Settings</h1><br>", unsafe_allow_html=True)

data = "data/datapop.xlsx"

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
                                usecols='A:G',
                                parse_dates=True)

                #Visualize population growth
                plost.area_chart(data, "Year", "Population", height=250, color='#0a81c0')
                plost.pie_chart(data, "Year", "Population", height=250)


                #visualize Annual population growth %
                #st.markdown("<p style='text-align: center; color: #fff; { font-family: finlandica; } '>Annual Population growth %</p><br>", unsafe_allow_html=True)
                if st.checkbox("Wanna see the annual population growth %? Click Here."):
                        plost.bar_chart(data, "Year", "Annual%", height=500, opacity=1.0, width=500, color="#ec5939")
#_____________________________________________________________________________________________________

        #FEMALES OF TOTAL POPULATION!
        elif selection == (female):

                '''**Female population growth in Finland 2000-2020**'''

                excel_file = "data/datapop.xlsx"

                data = pd.read_excel(excel_file,
                                usecols='A,D,F',
                                parse_dates=True)
                plost.area_chart(data, "Year", "Female", height=250, color='#673ba6')
                
                
                #OPTION FOR FEMALE POPULATION
                #data.set_index("Year", inplace=True)
                #selected_indices = st.multiselect('Select the Specific year.', data.index)
                #selected_rows = data.loc[selected_indices]
                #st.write(selected_rows)


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
                                usecols='A,C,E',
                                parse_dates=True)
                plost.area_chart(data, "Year", "Male", height=250, color='#424141')

                
                #OPTION FOR MALE POPULATION
                #data.set_index('Year', inplace=True)
                #selected_indices = st.sidebar.multiselect('Select the Specific year.', data.index)
                #selected_rows = data.loc[selected_indices]
                #st.sidebar.write(selected_rows)
                

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


#EVERYTHING ABOUT GDP STARTS HERE------------------------------------------------------------------------------------------------
st.markdown("<h1 style='text-align: center; color: #8892B0; { font-family: finlandica; } '><br>GDP</h1>", unsafe_allow_html=True)
st.write("Finland has the 4th largest knowledge economy in Europe, behind Sweden, Denmark and the UK. ")

data = pd.read_excel(data,
                        usecols='A,H',
                        parse_dates=True)
plost.line_chart(data, "Year", "GDP", color='#dcdf0e')
