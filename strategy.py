import yfinance as yf

from dataloader import load_data

def create_signals(data, short_window, long_window):

    #Calculates returns by finding percentage change of closing prices

    data["Return"]=data["Close"].pct_change()

    #Computes mean of closing prices over the short window and long window periods of time to find the short and long moving averages

    short_ma=data["Close"].rolling(short_window).mean()

    long_ma=data["Close"].rolling(long_window).mean()

    #Creates signal column where if short_ma > long_ma the signal is changed to 1 otherwise it remains as 0 and this acts as an indicator of whether we take a long position or not

    data["Signal"] = 0
    data.loc[short_ma > long_ma, "Signal"] = 1

    #Shifts all signal values down one to apply a 1-day lag to eliminate lookahead bias as it we did not do this we could use today's signal to trade on today's return

    data["Signal"]=data["Signal"].shift(1)

    #Removes n/a data caused by the shifting of the data

    data=data.dropna()

    return data