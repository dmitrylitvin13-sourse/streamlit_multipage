import streamlit as st
import pandas as pd
# import numpy as np
# import sys
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

# Main page content
# st.markdown("# page 1 👀")  
'## Page 1 👀. Matplotlib|seaborn bikes-ploting '
st.sidebar.markdown("# 1 👀. Matplotlib ")

'### bikes.head(3)'
bikes = st.session_state.bikes   # from multipage_app.py
st.write(bikes.head(3))
# print(bikes.columns)   # to terminal

'### Распределение по месяцам среднего значения числового параметра'
# Наименования только числовых колонок
# col_num = bikes.select_dtypes(include='number').columns
# col_num  # equal  st.write(col_num)
# print(col_num)
col_num = ['Temperature', 'Humidity', 'Wind speed', 'Rainfall', 'Snowfall', 'Rental Count']  
col = st.pills(':blue-background[Выбери параметр:]', col_num, default='Temperature')
# col = st.select_slider(":blue-background[Выбери параметр:]",  options=col_num, value='Rental Count'  )  # +
# st.write("My column is", col)

month_weather = bikes.groupby(bikes['Date'].dt.month)[[col,'Date']].mean()      # номер месяца
month_weather['month_fname'] = month_weather['Date'].dt.month_name()            # полное название месяца
month_weather['month_name'] = month_weather['Date'].dt.strftime('%b')           # краткое название месяца
# month_weather


# rainbow_colors = ["Blue", "Red", "Orange", "Yellow", "Green", "Indigo", "Violet"]
# color = st.select_slider(":blue-background[Select a color:]", options=rainbow_colors, ) # +
cms = ['autumn', 'viridis', 'brg', 'bwr', 'cool', 'coolwarm', 'copper',]
cm = st.pills(':blue-background[Select colormap:]', cms, default='viridis')

color_v = st.slider(f":blue-background[Select a color from colormap]:orange-background['{cm}':]", 0., 1., 0.75)
color = plt.get_cmap(cm)(color_v)   # 

# '##### Use matplotlib | sns `with st.pyplot(fig)`'  # можно заголовок любого уровня!
fig, ax = plt.subplots(figsize=(4,2), dpi=80)   # dpi не работает здесь

# ax.bar(month_weather.index, month_weather)
sns.barplot(x=month_weather['month_name'], y=month_weather[col], ax=ax, color=color)
ax.set_title(f'Monthly distribution `{col}`', fontsize=8)
ax.set_xticklabels(month_weather['month_name'], rotation=45)
ax.set_xlabel('')
st.pyplot(fig, )   # для отображения matplotlib or seaborm fig
 
#***************************************************
'#### Use matplotlib | sns `with st.pyplot(fig)`'  # можно заголовок любого уровня!
# группировка по неделям
bikes_week = st.session_state.bikes_week   # from multipage_app.py


col_num = ['Temperature', 'Humidity', 'Wind speed', 'Rental Count']  
# col = st.pills(':blue-background[Выбери параметр:]', col_num, default='Temperature')

col_x = st.selectbox('`st.selectbox` **по оси X** ', col_num, index=1 )  # preselect
# 'You selected: ', col_x
col_y = st.selectbox('`st.selectbox` **по оси Y** ', col_num, index=3) 
# 'You selected: ', col_y
# print(col_x, type(col_x))   # for debugging

df = bikes_week
fig, ax = plt.subplots(figsize=(4,2), dpi=80)   # dpi не работает здесь 
# ax.scatter(df[col_x], df[col_y])  # +  matplotlib
sns.scatterplot(x=df[col_x], y=df[col_y])  # + seaborn
# sns.regplot(x=df[col_x], y=df[col_y])  # + seaborn
ax.set_title('Группировка по неделям', fontsize=8)

# st.pyplot(fig, )   # для обображения plt fig
fig