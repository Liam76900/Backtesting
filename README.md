Markdown

Multi-Asset Backtesting of a Moving Average Crossover Strategy

#Overview

This project acts as a simulation of a moving average crossover trading strategy against a buy and hold strategy with mutiple different assets. It also simulatneously incorporates different parameter choices (moving average windows) which help to interpret how these conditions affect risk and returns.

#Features

-Multi-asset backtesting
-Many risk metrics including Sharpe Ratio, Maximum Drawdown and Annualised Volatility
-A set of parameter choices(window combinations)
-Moving Average Crossover Strategy
-Comparative data against a buy and hold strategy
-Graphical visualisations of Cumulative Returns and Drawdowns

#Method and Logic

Signals are generated depending on the relationship between short-term and long-term moving averages. When the short-term moving average surpasses the long-term moving average, a long position is taken. Conversely, when the short-term moving average sinks below the long-term moving average, the position is closed. These binary signals shows whether the strategy is exposed to price movements where 1 indicates you are in the market (long position) and, 0, out of the market.

Strategy returns are computed from the percentage change in  asset prices and multiplied by the signal to ensure that these returns are only being granted when the strategy is in a long position.

The cumulative performance of the strategy is calculated by compounding the strategy returns to mirror the growth of the investment progressively. This same technique is used for the cumulative market (buy and hold) returns as a control.

The Buy and Hold strategy makes the assumption that the investor buys at the start and holds it throughout the duration of the time. This then serves as a reference to observe whether the strategy adds value.

The risk metrics taken into account are the sharpe ratio, annualised volatility and maximum drawdown. Sharpe ratio measures risk-adjusted returns to perceive whether the returns made are in fact as valuable as the risk taken. Annualised volatility represents how variable the stock prices are with higher percentages indicating greater risk, and lower percentages, more stability. Max drawdowns takes into account the greatest peak-to-trough decline in stock value, demonstrating the worst potential outcome of an investment.

The strategy is also tested against a selection of different short-term and long-term windows of [5, 10, 20] and [20, 50, 100] days respectively. This, therefore, allows us to analyse the sensitivity of the strategy to the parameter choices made.

#Results

| Asset | MA Windows | Strategy Return (%) | Market Return (%) | Annualised Volatility (%) | Sharpe | Max Drawdown (%) |
|-------|------------|---------------------|-------------------|---------------------------|--------|------------------|
| AAPL  | 5  / 20    |      20.03          |       54.49       |         16.32             | 1.218  |     -14.69       |
| MSFT  | 5  / 20    |      20.43          |       58.03       |         19.61             | 1.061  |     -13.23       |
| GOOGL | 5  / 20    |     -0.992          |       56.43       |         24.80             | 0.084  |     -16.53       |
| AAPL  | 10 / 50    |      16.91          |       54.49       |         13.16             | 1.272  |     -12.64       |
| MSFT  | 10 / 50    |      34.62          |       58.03       |         19.62             | 1.637  |     -13.93       |
| GOOGL | 10 / 50    |      13.30          |       56.43       |         23.54             | 0.657  |     -19.59       |
| AAPL  | 20 / 100   |      08.99          |       54.49       |         10.68             | 0.872  |     -11.31       |
| MSFT  | 20 / 100   |      04.19          |       58.03       |         14.75             | 0.356  |     -13.07       |
| GOOGL | 20 / 100   |      12.99          |       56.43       |         20.59             | 0.706  |     -13.08       |

#Plot of Strategy Returns of all assets with the [5, 20]
 day window against time

<p align="center">
  <img src=".\images\five-twenty.png" alt="Moving Average" width="600"/>
</p>

#Plot of Strategy Returns of all assets with the [10, 50]
 day window against time

<p align="center">
  <img src=".\images\ten-fifty.png" alt="Moving Average" width="600"/>
</p>

#Plot of Strategy Returns Vs Market Returns of all assets with the [10, 50]
day window against time

<p align="center">
  <img src=".\images\ten-fifty-market-strategy.png" alt="Moving Average" width="600"/>
</p>

#Plot of Strategy Return Drawdowns of all assets with the [10, 50] day window against time

<p align="center">
  <img src=".\images\ten-fifty-d.png" alt="Moving Average" width="600"/>
</p>