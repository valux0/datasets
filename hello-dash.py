import streamlit as st
import pandas as pd
st.title("hello page")
st.write("karin es bello")
dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(dataframe)

