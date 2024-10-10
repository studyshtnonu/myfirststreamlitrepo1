import streamlit as st

st.header('st.checkbox')

st.write('what do you want for desert')

icecream = st.checkbox('icecream')
chocolate = st.checkbox('chocolate')

if icecream: 
    st.write("here is icecream")

if chocolate:
    st.write("here is chocolate")

    