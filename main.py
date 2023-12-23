import matplotlib.pyplot as plt
import streamlit as st
import datetime as dt
import apimoex as mx
import matplotlib
matplotlib.use('agg')


# demonstration data
ticker = 'SBER'
start = dt.date(2023, 1, 1)
end = dt.date(2023, 12, 31)
interval = 24

# Initial page content
st.title('Dashboard')
st.sidebar.title('Stock Parameters')
ticker = st.sidebar.text_input('Ticker', value=ticker)
start = st.sidebar.date_input('Start Date', value=start)
end = st.sidebar.date_input('End Date', value=end)

# checking the correctness of the entered data
description = mx.get_specification(ticker)
if description.empty:
    st.write('Error: invalid company ticker.')
else:
    # loading dashboard
    name = description.loc[1][2]
    candles = mx.get_market_candles(ticker, start, end, interval)
    fig, ax = plt.subplots(figsize=(10, 5))
    x = candles['end']
    y = candles['close']
    ax.plot(x, y)
    st.header(f'{name} Stock Quote')
    st.pyplot(fig)

    dividends = mx.get_dividends(ticker)
    st.header('Dividends')
    st.write(dividends)
