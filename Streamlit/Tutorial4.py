import streamlit as st 
import pandas as pd 
#basic knowldge of pandas

st.title("File Uploading")

file=st.file_uploader("Upload your File",type=['csv'])

if file:
    df=pd.read_csv(file)
    st.write("Your Data")
    st.dataframe(df)
else:
    st.write("No Data to Show")

if file:
    st.write("Summary")
    st.dataframe(df.describe())

if file:
    unique_marks=df['Marks'].unique()
    marks_select=st.selectbox("Select Marks",unique_marks)
    filter= df[df['Marks']==marks_select]
    st.write("Filtered Data")
    st.dataframe(filter)







