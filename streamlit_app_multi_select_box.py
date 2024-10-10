import streamlit as st

st.header('st.multselect')

option = st.multiselect(
    'What color do you like ',
    ['blue','yellow'],
    ['red','green'])


st.write('selected color is : ',option)
