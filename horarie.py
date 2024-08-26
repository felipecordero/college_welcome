import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",)
# st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", unsafe_allow_html=True)
df = pd.read_csv("horaire.csv", sep=";")
df = df.replace("Drishti kaushik", "Drishti Kaushik")
df = df.replace("Edaurdo Cuellar", "Eduardo Cuellar")
df = df.replace("Vishal", "Vishal Saha")
df = df.replace("Javieera Guzman", "Javiera Guzman")
df.ffill(inplace=True)
names = df.iloc[:, 2:].stack().unique().tolist()
names.sort()
col1, col2 = st.columns(2)
col1.image("logo.png", width = 50)
col2.subheader("Welcome Team \n Schedule 26 -> 30")
user = st.selectbox(options = names, label = "Select User")
days = df.columns[2:]
day = st.selectbox(options = days, label = "Select Day")
st.dataframe(df[["Horarie", "Position", day]][df[day] == user], hide_index=True, width=600,)