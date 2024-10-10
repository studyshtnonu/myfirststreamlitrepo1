import streamlit as st
from datetime import time , datetime

st.subheader('st.slider')

age = st.lslider('How Old Are You?', 0, 15,25)
st.write('I am',age,' old')