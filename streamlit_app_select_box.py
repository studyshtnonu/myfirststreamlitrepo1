import streamlit as st

st.header('st.selectbox')

option = st.selectbox("What colr do you want?",('blue','yellow','orange'))
st.write('The selected color is ',option)