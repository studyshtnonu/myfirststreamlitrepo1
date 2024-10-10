import streamlit as st
from datetime import time , datetime

st.subheader('st.slider')

age = st.slider('How Old Are You?', 0, 15,25)
st.write('I am',age,' old')

st.subheader('st.range')

values_between = st.slider('select a set of range',0.0,100.0,(25.0,50.0))
st.write(values_between)

st.subheader('range_time')
appointment = st.slider ('select your appointment', value=(time(11, 30), time(12, 45)))
st.write('your selected appointment is',appointment)

