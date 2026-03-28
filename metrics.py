import numpy as np

def calculate_metrics(data):

    #Computes sharpe ratio to analyse risk-adjusted returns

    sharpe_ratio=(data["Net_Strategy_Returns"].mean() / data["Net_Strategy_Returns"].std()) * np.sqrt(252)

    #Computes annualised volatility to quantify risk

    annualised_volatility=(data["Net_Strategy_Returns"].std() * np.sqrt(252))

    #Computes maximum drawdown to indicate the greatest possible loss

    data["Rolling_Max"]=data["Cumulative_Strategy"].cummax()
    data["Drawdown"]=data["Cumulative_Strategy"] / data["Rolling_Max"] - 1
    max_drawdown=data["Drawdown"].min()

    return sharpe_ratio, annualised_volatility, max_drawdown