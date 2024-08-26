def ma_testing(symbol,ltp,all_high,ma_20,ma_50):
    if(ma_20>ma_50):
        # print(symbol,'ma_pass')
        hello = 1

def go_testing(symbol, stock_data):
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

    ma_testing(symbol,ltp,all_high,ma_20,ma_50)