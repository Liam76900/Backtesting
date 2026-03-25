def backtesting(data):
    data["Strategy_Returns"]=data["Signal"] * data["Return"]
    
    data["Cumulative_Market"]=(1+data["Return"]).cumprod()
    data["Cumulative_Strategy"]=(1+data["Strategy_Returns"]).cumprod()

    return data