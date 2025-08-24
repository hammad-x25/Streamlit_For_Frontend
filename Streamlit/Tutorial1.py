import streamlit as st

#Set the Title
st.title("Hello world")

#With subheader
st.subheader("With streamlit")

#To write 
st.text("Welcome with text")
st.write("Welcome with write text")

choice = st.selectbox("Your fav Language:",[ 'Python','C++','Rust ','JS','Java'])

# Displaying variable 
st.write(f"your choice {choice}")

st.success("Your first tutorial has been completed")