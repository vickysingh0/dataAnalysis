import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Vickystore", page_icon=":bar_chart:", layout="wide")
# st.write("data")#it is work as console of js which print every thing to the app
# st.write("data1")

st.title(":bar_chart: Sample stote EDA") 
st.markdown('<style>div.block-container{padding-top:1rem;} </style>',unsafe_allow_html=True)

fl= st.file_uploader(":file_folder: upload a file", type=(["csv","txt","xlsx","xls"]))
                     
if fl is not None:
    filename= fl.name
    st.write(filename)
    df=pd.read_excel(filename, encoding="ISO-8859-1")
else:
#    os.chdir(r"P:\streamlite")
    df = pd.read_excel("tips.csv", encoding="ISO-8859-1")

data=df.columns

st.write(data)