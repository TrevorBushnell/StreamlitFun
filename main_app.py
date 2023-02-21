import streamlit as st
import pandas as pd
import numpy as np

'''

'''
st.write("""
# My First Streamlit Webpage

And then here is some more text. Here is a live update!
""")

df = pd.read_csv('./data.csv')
st.write(df)

options = st.selectbox('Which option do you want:', ['show plotting feature', 'show slider feature'])

if options == 'show plotting feature':

    if st.checkbox('Show plotting feature:'):
        sample_df = pd.DataFrame(
            np.random.randn(10,3),
            columns=['a','b','c']
        )
        st.line_chart(sample_df)

elif options == 'show slider feature':  
    x = st.slider('x')
    st.write('2 times x is', 2*x)