import streamlit as st

st.header('st.button')

if st.button('Hello'):
   st.write('hello dear')
elif st.button('hi'):
   st.write('hi dear')
else:
   st.write('goodbye!')

