import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write('welcome to my world')

st.header('st.write')

st.write('hello dear')
st.write('time is 8:30')

df = pd.DataFrame({
    'first_column': [1,2,3,4],
    'second_column':[12,13,14,15]
    })

st.write(df)


st.write('Below is the Dataframe df',df,'above is the datframe')

df2 = pd.DataFrame(
    np.random.randn(5,3),
    columns=['a','b','c']
    )

        
c = alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
    )

st.write(c)

