import streamlit as st
import pandas as pd

file_path = 'C:\Users\shail\OneDrive\Desktop\WhisperOpenAI\audio_files\housing.csv"
df = pd.read_csv(file_path)
print(df.head())
