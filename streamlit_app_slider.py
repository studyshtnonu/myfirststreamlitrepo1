import streamlit as st
from datetime import time , datetime

st.subheader('st.slider')

age = st.slider('How Old Are You?', 0, 15,25)
st.write('I am',age,' old')

st.subheader('st.range')

values_between = st.slider('select a set of range',0.0,100.0,(25,50))
st.write(values_between)

