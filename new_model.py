import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import warnings
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from symbols import stock_symbols
from testing import  go_testing
warnings.filterwarnings("ignore", message="The 'unit' keyword in TimedeltaIndex construction is deprecated.*")

Stocks = []
nifty_200_symbols = stock_symbols()
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=5*365)).strftime('%Y-%m-%d')
nifty_200_data = pd.DataFrame()

#creating a data frame which have 6 columns (Symbol, Date, Close, open , HIgh, low) and  rows with all symbols for every Date
for symbol in nifty_200_symbols:
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        stock_data = stock_data.reset_index()  # Reset index to have 'Date' as a column
        stock_data['Symbol'] = symbol  # Add a column for stock symbol
        stock_data = stock_data[['Symbol', 'Date', 'Close', 'Open','Low','High','Volume']]
        nifty_200_data = pd.concat([nifty_200_data, stock_data])
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

#calculating stock metrics
for symbol in nifty_200_symbols:
    stock_data = nifty_200_data[nifty_200_data['Symbol'] == symbol]
    stock_data= stock_data.copy()

    ma_20= stock_data['Close'].tail(20).mean()
    ma_50= stock_data['Close'].tail(50).mean()
    ma_200 = stock_data['Close'].tail(200).mean()
    all_high = stock_data['Close'].max()
    ltp = stock_data['Close'].iloc[-1]
    share_details = yf.Ticker(symbol)
    share_history = share_details.history()
    delta_today = share_history['Close'].iloc[-1] - share_history['Open'].iloc[-1]
    body_today = share_history['High'].iloc[-1] - share_history['Low'].iloc[-1]
    three_forth = (0.7 * body_today) + share_history['Low'].iloc[-1]
    
    if (ma_50 > ma_200) and (ltp>three_forth):
        go_testing(symbol, stock_data)


        


    





        

