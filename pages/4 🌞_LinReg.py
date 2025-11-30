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
    layout="centered",  # wide
    page_title="LinReg",
    page_icon="🌞",
    )

"## Page 4 🌞. LinReg"
st.sidebar.markdown("# 4🌞. corr")

funcs = ['a*x+b', 'sin((a*x+b)*pi)', 'ln(a*x+b)', '1/(a*x+b)']  
func = st.pills(':blue-background[Select function:]', funcs, default='a*x+b')

with st.sidebar:
    a = st.slider('a', 0.5, 4., 1.)
    b = st.slider('b', -1., 1., 0.)
    rnd_m = st.slider('rnd value', 0., 2., 0.5)

x = np.linspace(.01, 1)

if 'rnd' not in st.session_state:     # исходное случайное распределение
    st.session_state.rnd = (np.random.random(len(x)) -0.5)
    
if st.sidebar.button('Reset rnd'):
    st.session_state.rnd = (np.random.random(len(x)) -0.5)
    
rnd = st.session_state.rnd * rnd_m
lin = x*a + b + rnd
sin = np.sin((x*a + b)*np.pi ) + rnd
ln = np.log(x*a + b) + rnd
inv = 1/(x*a + b) + rnd

dict_f = {'a*x+b':lin, 'sin((a*x+b)*pi)':sin, 'ln(a*x+b)':ln, '1/(a*x+b)':inv}

fig, ax = plt.subplots(figsize=(7,4), dpi=80)
sns.regplot(x=x, y=dict_f[func], ax=ax, label=func)
# sns.regplot(x=x, y=sin, ax=ax, label='sin')
# sns.regplot(x=x, y=ln, ax=ax, label='ln')
# sns.regplot(x=x, y=inv, ax=ax, label='inv')
ax.set_xlim(0,1)
ax.set_ylim(-2,3)
ax.grid(True)
ax.legend()
plt.tight_layout()

'## Use `sns.regplot`', f':orange-background[corr = {np.corrcoef(x, dict_f[func])[0,1]:.2f}]'
st.pyplot(fig)
# st.pyplot(plt.gcf())

