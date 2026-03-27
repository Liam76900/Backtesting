def backtesting(data):
    data["Strategy_Returns"]=data["Signal"] * data["Return"]

    cost=0.001

    data["Trade"]=data["Signal"].diff().abs()

    data["Transaction_Costs"]=data["Trade"] * cost

    data["Net_Strategy_Returns"]=data["Strategy_Returns"] - data["Transaction_Costs"]

    data["Market_Transaction_Costs"]=0.0

    data.loc[data.index[0], "Market_Transaction_Costs"] = cost
    data.loc[data.index[-1], "Market_Transaction_Costs"] = cost

    data["Net_Market_Returns"]=data["Return"] - data["Market_Transaction_Costs"]
    data["Cumulative_Market"]=(1+data["Net_Market_Returns"]).cumprod()
    data["Cumulative_Strategy"]=(1+data["Net_Strategy_Returns"]).cumprod()

    return data