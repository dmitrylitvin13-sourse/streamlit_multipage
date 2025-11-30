
import streamlit as st
import pandas as pd
import sys
# import os
# print(os.getcwd())
# # 
# https://docs.python.org/3/tutorial/venv.html
# pip install -r requirements.txt
# to run from "D:\...\Python\VSC\multipage":   streamlit run multipage_app.py

# st.set_page_config(layout="wide")
# st.set_page_config(layout="centered")  # default

# Define the pages
#  emoji from  https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
#              https://getemoji.com/
pages = [
    st.Page("page_1.py", title="Page 1", icon="👀"), # "":eyes:"
    st.Page("page_2.py ", title="Page 2", icon="📈"),  # ":chart_with_upwards_trend:"
    st.Page("page_3.py", title="Page 3", icon="🚀"), # ":rocket:"
    st.Page("page_4.py", title="Page 4", icon="🌞"), # ":sun_with_face:"
]


# Set up navigation
# pg = st.navigation([page_1, page_2, page_3, page_4])
pg = st.navigation({'Pages:' : pages})

@st.cache_data                 # 👈 Add the caching decorator
def load_data(url):
    # df = pd.read_csv(url) 
    df = pd.read_pickle(url)    # 👈 Download the data
    return df

bikes = load_data('BikesDataImputed.pkl')

if 'bikes' not in st.session_state:
    st.session_state.bikes = bikes

@st.cache_data
def transform(df):
    # группировка по неделям
    rental_sum = df.groupby(df['Date'].dt.isocalendar().week)['Rental Count'].sum()
    temp_mean = df.groupby(df['Date'].dt.isocalendar().week)['Temperature'].mean()
    humidity_mean = df.groupby(df['Date'].dt.isocalendar().week)['Humidity'].mean()
    wind_mean = df.groupby(df['Date'].dt.isocalendar().week)['Wind speed'].mean()
    df_week = pd.concat([rental_sum, temp_mean, humidity_mean, wind_mean], axis=1)
    return df_week 

bikes_week = transform(bikes)

if 'bikes_week' not in st.session_state:
    st.session_state.bikes_week = bikes_week

   
# Run selected pages
pg.run()