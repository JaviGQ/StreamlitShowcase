import streamlit as st
import requests

st.title("Crypto Monitoring")
st.header("Find the latest Cryptocurrency Price Updates")

crypto = st.sidebar.selectbox("Choose a cryptocurrency", options=[
    "", "Bitcoin", "Litecoin", "Ethereum"])

def api_url(from_, to_):
    return f"https://min-api.cryptocompare.com/data/price?fsym={from_}&tsyms={to_}"

if crypto == "Bitcoin":
    api_url = api_url("BTC", "USD")
    response = requests.get(api_url).json()
    #st.json(response)

    btc_price = response["USD"]
    st.success(f"The current price of {crypto} is US ${btc_price:.2f}.")

elif crypto == "Litecoin":
    api_url = api_url("LTC", "USD")
    response = requests.get(api_url).json()
    ltc_price = response["USD"]
    st.success(f"The current price of {crypto} is US ${ltc_price:.2f}.")

elif crypto == "Ethereum":
    api_url = api_url("ETH", "USD")
    response = requests.get(api_url).json()
    eth_price = response["USD"]
    st.success(f"The current price of {crypto} is US ${eth_price:.2f}.")

else:
    st.info("Please choose a cryptocurrency to check the price in in US$.")