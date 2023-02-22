import streamlit as st
import pandas as pd
import numpy as np
import utils
import matplotlib.pyplot as plt


st.write("""
# This Is Our First Streamlit App

Here is our first line of text in our Streamlit app!
""")

df = pd.read_csv('./data.csv')
df = utils.clean_dataframe(df)
df

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)

options = st.selectbox('choose what feature you want to display!', ['graphing feature', 'textbox feature', 'slider feature', 'matplotlib feature'])
st.write(options)

if options == 'graphing feature':
    st.line_chart(chart_data)

elif options == 'slider feature':
    x = st.slider('x')
    st.write('2 times x is', 2*x)

elif options == 'textbox feature':
    text_input = st.text_input('type your name here')
    st.write(text_input)

elif options == 'matplotlib feature':
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    st.pyplot(fig)