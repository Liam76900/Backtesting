import yfinance as yf

def load_data(symbol):
    data = yf.download(symbol, start="2023-01-01", end="2024-01-01")
    data.columns = data.columns.droplevel(1)
    return data