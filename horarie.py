import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",)

def cleanText(x: str):
    # return x.split(".")[1].split()[0].strip()
    try:
        return x.split(".")[1].split()[0].strip()
    except:
        return x

df = pd.read_csv("horaire_3_6.csv", sep=",")

# Apply the cleanText function to each column in the DataFrame slice
for col in df.columns[2:]:
    df[col] = df[col].apply(cleanText)

df.iloc[:, 0:2] = df.iloc[:, 0:2].ffill()
names = df.iloc[:, 2:].stack().unique().tolist()
names.sort()
col1, col2 = st.columns(2)
col1.image("logo.png", width = 50)
col2.subheader("Welcome Team \n Schedule 3 -> 6 Sept.")
user = st.selectbox(options = names, label = "Select User")
days = df.columns[2:]
day = st.selectbox(options = days, label = "Select Day")
st.dataframe(df[["Heure", "Position", day]][df[day] == user], hide_index=True, width=600,)