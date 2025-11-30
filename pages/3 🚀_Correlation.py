import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import sys
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    layout="wide",  # wide or centered
    page_title="Correlation",
    page_icon="🚀",
    )

"## Page 3 🚀. Correlation"
st.sidebar.markdown("# 3🚀. corr")

# группировка по неделям
bikes_week = st.session_state.bikes_week   # from multipage_app.py
bikes_week.tail(2)

column1, column2 = st.columns([2, 3], border=True)
with column1:
    '## Use `sns.pairplot()`'
    # fig = plt.figure(figsize=(8,6))
    fig, ax = plt.subplots(figsize=(8,6))
    sns.pairplot(bikes_week, kind='scatter', diag_kind='kde', height=1.4, aspect=1.2,) # kernel density estimate
    # plt.title("sns.pairplot")   # не отображает
    # ax.set_title("sns.pairplot")   # не отображает
    st.pyplot(plt.gcf())
    # st.pyplot(fig)     # не отображает

with column2:
    '## df.corr()'
    st.write(bikes_week.corr())   
    # st.dataframe(bikes_week.corr())    # equal

    '## sns.heatmap()'
    fig, ax = plt.subplots(1,2, figsize = (12,4), dpi=80)

    correlation = bikes_week.corr()

    sns.heatmap(correlation, ax=ax[0],vmax=1, vmin=-1,
                linewidths=0.5, annot=True, cmap='vlag',                 # viridis, coolwarm
                linecolor="white", annot_kws = {'size':12})

    sns.heatmap(correlation, ax=ax[1],vmax=1, vmin=-1, mask=np.triu(correlation, k=0),
                linewidths=0.5, annot=True, cmap='vlag',               # viridis, coolwarm
                linecolor="white", annot_kws = {'size':12})
    plt.tight_layout()

    st.pyplot(fig)
    # st.pyplot(plt.gcf())
