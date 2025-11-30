import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

"## Page 2 📈. Seaborn, plotly_exspress"
'### :blue-background[<- 👈 Select params with sidebar]'
st.sidebar.markdown("# 2 📈. sns, px")

bikes = st.session_state.bikes   # from multipage_app.py
# st.write(bikes.tail(2))

# группировка по неделям
bikes_week = st.session_state.bikes_week   # from multipage_app.py

# Наименования только числовых колонок
col_num = ['Temperature', 'Humidity', 'Wind speed', 'Rental Count']  
# col_num = bikes_week.columns   # equal
# col_num  # equal  st.write(col_num)

with st.sidebar:
    col_x = st.selectbox('`st.selectbox` **по оси X** ', col_num, index=1 )  # preselect
    # 'You selected: ', col_x
    col_y = st.selectbox('`st.selectbox` **по оси Y** ', col_num, index=3) 
    # print(col_x, type(col_x))   # for debugging

# ******************************************************************
'### Use `sns.regplot()` and `st.pyplot(fig)`',\
    f':orange-background[corr = {bikes_week[col_x].corr(bikes_week[col_y]):>20.2f}]'
# st.subheader(f':orange-background[corr = {bikes_week[col_x].corr(bikes_week[col_y]):>20.2f}]')

left_column, right_column = st.columns([2,3], border=True)
with left_column:
    if st.checkbox('Show all data'):
        bikes_week[[col_x, col_y]]
    else:
        bikes_week[[col_x, col_y]].iloc[:3,:]  # only some rows
                
with right_column:
    df = bikes_week
    fig, ax = plt.subplots(figsize=(4,2), dpi=80)   # dpi не работает здесь
    # st.line_chart(bikes, x=col_x, y=col_y)
    # st.scatter_chart(bikes, x=str(col_x), y=str(col_y))
    sns.regplot(x=df[col_x], y=df[col_y], ax=ax)  # + seaborn
    # ax.set_title()
    st.pyplot(fig)
    

# ******************************************************************
'### Use `px.scatter()` and `st.plotly_chart(fig)`'

fig = px.scatter(df, x=col_x, y=col_y, )
# fig = px.line(bikes, x=col_x, y=col_y, )
# Plot!
st.plotly_chart(fig)  # для отрисовки px.figure


