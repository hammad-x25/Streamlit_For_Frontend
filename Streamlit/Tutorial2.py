import streamlit as st
one=''
two=''
if st.button("Click me"):
    one = st.success("You clicked the button")
    # Set Title
    st.title("Button 1 Clicked!")
if st.button("Click me too"):
    two=st.success("You clicked the second button")
    # Set Title
    st.title("Button 2 Clicked!")
list1=['OOP','DSA','DYNAMIC PROGRAMMING','ML','AI']

for x in list1:
   ok=st.checkbox(f"{x}")
   




level = st.slider("Expreince Level in Years:",0,10,2)




lang=st.selectbox("Select your favorite programming language:",['Python','C++','Rust ','JS','Java'])

name=st.text_input("Enter your name:")


textarea=st.text_area("Enter your address:")


datew=st.date_input("Enter your date of birth:")
    
rate=st.radio("How would you rate your experience with Streamlit so far?",['Excellent','Good','Average','Poor'])    

if rate:
    st.number_input("On a scale of 1 to 10, how likely are you to recommend Streamlit to a friend or colleague?",1,10,5)
if name:
    st.write(f"Your name is {name}")
if textarea:  
    st.write(f"Your address is {textarea}")
if datew:
    st.write(f"Your date of birth is {datew}")

if lang:
    st.write(f"Your favorite programming language is {lang}")    

st.write(f"Your Expreince Level is {level} years")



