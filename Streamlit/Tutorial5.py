import streamlit as st
import requests
import numpy as np
import pandas as pd

st.title("Currency Converter")

def get_exchange_rate(base_currency, target_currency,amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        return rate*amount
    else:
        st.error("Error fetching exchange rates.")
        return None
    

base_currency = st.selectbox("Select Base Currency", ["USD", "EUR", "GBP", "INR",'PKR'])
target_currency = st.selectbox("Select Target Currency", ["USD", "EUR", "GBP", "INR",'PKR'])
amount = st.number_input("Enter Amount", min_value=0.0)
if st.button("Convert"):
    if amount >= 0:
        converted_amount = get_exchange_rate(base_currency, target_currency,amount)
        if converted_amount is not None:
            st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        st.error("Please enter a valid amount.")


if st.button("Full Details"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()     
        df = pd.DataFrame(data["rates"], index=['Rate'])
        st.dataframe(df)
    else:
        st.error("Error fetching exchange rates.")


   