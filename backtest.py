def backtesting(data):
    data["Strategy_Returns"]=data["Signal"] * data["Return"]
    data["Trade"]=data["Signal"].diff().abs()

    cost=0.001

    data["Transaction_Costs"]=data["Trade"] * cost

    data["Net_Returns"]=data["Strategy_Returns"]-data["Transaction Costs"]

    data["Market_Transaction_Costs"]=0
    data.iloc(0, data.columns.get_loc("Market_Transaction_Costs")) = cost
    data.iloc(-1, data.columns.get_loc("Market_Transaction_Costs")) = cost
    data["Net_Market_Returns"]=data["Returns"] - data["Market_Transaction_Costs"]
    data["Cumulative_Market"]=(1+data["Return"]).cumprod()
    data["Cumulative_Strategy"]=(1+data["Net Returns"]).cumprod()

    return data