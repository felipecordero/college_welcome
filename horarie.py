import streamlit as st
import pandas as pd
st.set_page_config(layout="wide",)
# st.markdown("""
#     <style>
#         .reportview-container {
#             margin-top: -2em;
#         }
#         #MainMenu {visibility: hidden;}
#         .stDeployButton {display:none;}
#         stDecoration {display:none;}
#         footer {visibility: hidden;}
#         #stDecoration {display:none;}
#     </style>
# """, unsafe_allow_html=True)
# st.markdown(" <style> div[class^='st-emotion-cache-12fmjuu ezrtsby2'] { padding-top: -2rem; display:none} </style> ", unsafe_allow_html=True)
df = pd.read_csv("horaire.csv", sep=";")
df = df.replace("Drishti kaushik", "Drishti Kaushik")
df = df.replace("Edaurdo Cuellar", "Eduardo Cuellar")
df = df.replace("Vishal", "Vishal Saha")
df = df.replace("Javieera Guzman", "Javiera Guzman")
df.iloc[:, 0:2] = df.iloc[:, 0:2].ffill()
names = df.iloc[:, 2:].stack().unique().tolist()
names.sort()
col1, col2 = st.columns(2)
col1.image("logo.png", width = 50)
col2.subheader("Welcome Team \n Schedule 26 -> 30")
user = st.selectbox(options = names, label = "Select User")
days = df.columns[2:]
day = st.selectbox(options = days, label = "Select Day")
st.dataframe(df[["Horarie", "Position", day]][df[day] == user], hide_index=True, width=600,)