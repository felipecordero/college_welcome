import streamlit as st

import pandas as pd

st.set_page_config(
    layout="wide",
)

df = pd.read_csv("horaire.csv", sep=";")

df.ffill(inplace=True)

names = df.iloc[:, 2:].stack().unique().tolist()

user = st.sidebar.selectbox(options = names, label = "Select User")

days = df.columns[2:]

day = st.sidebar.selectbox(options = days, label = "Select Day")

st.dataframe(df[["Horarie", "Position", day]][df[day] == user], hide_index=True, width=600,)

