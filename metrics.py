import numpy as np

def calculate_metrics(data):

    sharpe_ratio=(data["Net_Strategy_Returns"].mean() / data["Net_Strategy_Returns"].std()) * np.sqrt(252)

    annualised_volatility=(data["Net_Strategy_Returns"].std() * np.sqrt(252))

    data["Rolling_Max"]=data["Cumulative_Strategy"].cummax()
    data["Drawdown"]=data["Cumulative_Strategy"] / data["Rolling_Max"] - 1
    max_drawdown=data["Drawdown"].min()

    return sharpe_ratio, annualised_volatility, max_drawdown