import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plost
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit.commands.page_config import set_page_config
import streamlit.components.v1 as components
import xlrd




#Simple way to display your data, for this we have used population data of Finland.
#I did this while learning about Streamlit.
#Be free to use and customize this code, experiment and try new things.
#- Elmeri Keitaanranta, 17. 


#set_page_config sets a title on your window.
st.set_page_config(page_title="Data Finland", layout="centered",
                                page_icon="images/suomi.png",
                                initial_sidebar_state="expanded")

#Top Headings
st.markdown("<h1 style='text-align: center; color: #C3C3C3; { font-family: finlandica; } '>Data Finland!</h1>",
        unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #C3C3C3; { font-family: finlandica; } '>Created by Elmeri Keitaanranta</p><br>",
        unsafe_allow_html=True)

st.sidebar.markdown("<h1 style='text-align: center; color: #8892B0; { font-family: finlandica; } '>Settings</h1><br>",
        unsafe_allow_html=True)

data = "data\datapop1.xlsx"

#function for viewing population data when clicked certain button on screen.
def choose():

        #Select what will be shown
        total = "Population Growth Finland"
        female = "Females in Finland"
        male = "Males in Finland"
        selection = st.sidebar.radio("Select what chart will be shown.", [total, female, male])

        #For positioning
        col1, col2, col3= st.columns((1,1,0.5))


        #TOTAL POPULATION
        if selection == (total):
                data = "data/data.xlsx"
                data = pd.read_excel(data, usecols="A,B")
                '''**Population growth in Finland 2000-2020**'''
                ### --- LOAD DATAFRAME

                #Visualize population growth
                plost.area_chart(data, "Year", "Population", height=250, color='#0a81c0')
                plost.pie_chart(data, "Year", "Population", height=250)
#_____________________________________________________________________________________________________

        #FEMALES OF TOTAL POPULATION!
        elif selection == (female):
                data = "data/data.xlsx"
                data = pd.read_excel(data, usecols="A,D")

                with col2:
                        st.metric("Females of Total Population", "50.69%", "-0.01%, since 2019",)
                "Female population growth"
                plost.area_chart(data, "Year", "Female", height=250, color='#673ba6')
                
#_________________________________________________________________________________________________________________

        #MALES OF TOTAL POPULATION!
        elif selection == (male):
                data = "data/data.xlsx"
                data = pd.read_excel(data, usecols="A,C")
                with col2:
                        st.metric("Males of Total Population", "49.32%", "0.02%, since 2019",)
                "Male population growth"
                plost.area_chart(data, "Year", "Male", height=250, color='#8f2f03')
                
        else:
                '''Error! Please visit the app again soon!'''
choose()




#-----GDP------
st.markdown("<h2 style='text-align: left; color: #C3C3C3; { font-family: finlandica; } '>GDP</h2>", unsafe_allow_html=True)
"GDP is the total of all value added created in an economy."


#chart = alt.Chart(data).mark_area(color="lightblue",interpolate='step-after', line=True).encode(
        #x=alt.X('Year', axis=alt.Axis(labelOverlap="greedy",grid=False)),
        #y=alt.Y('GDP'))
#st.altair_chart(chart, use_container_width=True)


def gdp():
        data = "data/data.xlsx"
        data = pd.read_excel(data, usecols="A,H")
        data.set_index('Year', inplace=True)


        #For positioning
        col1, col2, col3= st.columns((1,1,0.5))

        #Creates multiselect for GDP
        selected_indices = st.multiselect('Select the specific year to see it\'s GDP', data.index)
        selected_rows = data.loc[selected_indices]
        with col2:
                st.write(selected_rows)
        
        #GDP% chart
        data = "data/data.xlsx"
        data = pd.read_excel(data, usecols="A,I")
        plost.area_chart(data, "Year", "GDP%", height=250, color='#0b590a')

        st.caption('"Finland fell into recession in the last quarter of 2008, and it\'s economy did not begin growing again until the third quarter of 2009." - IndiaTimes.com')


        #GDP SETTINGS STARTS HERE
        data = "data/data.xlsx"
        data = pd.read_excel(data, usecols="A:K")

        #GDP SETTINGS HEADER
        st.sidebar.markdown("<h2 style='text-align: center; color: #8892B0; { font-family: finlandica; } '>GDP</h2>",
        unsafe_allow_html=True)

        #Global rank
        st.sidebar.write("Finland is ranked 42nd by it's GDP.")

        ""
        ""

        col6, col7 = st.columns((2,1))

        with col6:
                #Per Capita checkbox
                perCapita = st.sidebar.checkbox("GDP per Capita")
                if perCapita:
                        "per capita"
                        plost.bar_chart(data, "Year", "GDP-per-c", height=250, color='#0b590a')
        
        with col7:
                #Per Capita checkbox
                inflation = st.sidebar.checkbox("GDP Inflation")
                if inflation:
                        "inflation"
                        plost.bar_chart(data, "Year", "infaltion-GDP", height=250, color='#0b590a')

gdp()








