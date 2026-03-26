import numpy as np

def calculate_metrics(data):

    sharpe_ratio=(data["Strategy_Returns"].mean() / data["Strategy_Returns"].std()) * np.sqrt(252)

    annualised_volatility=(data["Strategy_Returns"].std() * np.sqrt(252))