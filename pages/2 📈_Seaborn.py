import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    layout="wide",  # wide or centered
    page_title="Seaborn",
    page_icon="📈",
    )

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
"""

"""

column1, column2, column3 = st.columns([1.5, 1.5, 2], border=True)
with column1:
    '### Origin data'
    if st.checkbox('Show all data', value=True):
        bikes_week[[col_x, col_y]]
    else:
        bikes_week[[col_x, col_y]].iloc[:3,:]  # only some rows
                
with column2:
    '### Use `sns.regplot()`', f':orange-background[corr = {bikes_week[col_x].corr(bikes_week[col_y]):>20.2f}]'
    df = bikes_week
    fig, ax = plt.subplots(figsize=(4,6), dpi=80)   # dpi не работает здесь
    # st.line_chart(bikes, x=col_x, y=col_y)
    # st.scatter_chart(bikes, x=str(col_x), y=str(col_y))
    sns.regplot(x=df[col_x], y=df[col_y], ax=ax)  # + seaborn
    # ax.set_title()
    st.pyplot(fig)

with column3:
    '### Use `px.scatter()` and `st.plotly_chart(fig)`'

    fig = px.scatter(df, x=col_x, y=col_y )
    fig.update_traces(marker=dict(color='darkgreen', size=12))
    # fig = px.line(bikes, x=col_x, y=col_y, )
    # Plot!
    st.plotly_chart(fig)  # для отрисовки px.figure


