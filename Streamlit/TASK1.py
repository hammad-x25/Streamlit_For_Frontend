import streamlit as st

st.header("Welcome to the Streamlit Task")
st.subheader("This is a simple DOB Calculating app")

one = st.date_input("Enter your date of birth:")
two = st.date_input("Enter today's date:")

if one or two:
    age =  two.year - one.year 
    st.write(f"Your age is approximately {age} years.")