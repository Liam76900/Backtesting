import yfinance as yf

from dataloader import load_data

def create_signals(data, short_window, long_window):

    data["Return"]=data["Close"].pct_change()

    short_ma=data["Close"].rolling(short_window).mean()

    long_ma=data["Close"].rolling(long_window).mean()

    data["Signal"] = 0
    data.loc[short_ma > long_ma, "Signal"] = 1

    data["Signal"]=data["Signal"].shift(1)

    data=data.dropna()

    return data