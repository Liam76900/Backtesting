from dataloader import load_data
from strategy import create_signals
from backtest import backtesting

windows=[(5,20),(10,50),(20,100)]
symbols=["AAPL","MSFT","GOOGL"]

for short_window,long_window in windows:
    for symbol in symbols:

        data=load_data(symbol)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)

        print(f"Results for {symbol} for {short_window} day short window and {long_window} day long window is")
        print(data[["Cumulative_Market", "Cumulative_Strategy"]].tail())