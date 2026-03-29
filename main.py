import matplotlib.pyplot as plt
from dataloader import load_data
from strategy import create_signals
from backtest import backtesting
from metrics import calculate_metrics

#Assigns the different parameters for the windows of time and the different assets so we can cycle through them in our loops

windows=[(5,20),(10,50),(20,100)]
assets=["AAPL","MSFT","GOOGL"]

#Loops through the different parameters for the windows of time

for short_window,long_window in windows:

    #Creates a new figure for our plot as we will be plotting two graphs each loop

    plt.figure(figsize=(10, 5))

    #Loops through the different assets to load its specific stock data

    for asset in assets:

        #Assigned variables are ran through the different defined functions

        data=load_data(asset)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)
        sharpe_ratio, annualised_volatility, max_drawdown=calculate_metrics(data)

        #Outputs the dataframe for cumulative market and strategy return values

        print(f"Results for {asset} for {short_window} day short window and {long_window} day long window is")
        print(data[["Cumulative_Market", "Cumulative_Strategy"]].tail())

        #Outputs risk metrics

        print("Sharpe ratio:")
        print(sharpe_ratio)
        print("Annualised Volatility:")
        print(annualised_volatility)
        print("Max Drawdown:")
        print(max_drawdown)

        #Plots cumulative strategy returns of all the different asssets over the time frame

        plt.plot(data["Cumulative_Strategy"], label=asset)

    #Adds legend, axis labels, title, gridlines to graph and returns the graph

    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.title("Strategy Returns Over Assets")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    #Creates a new figure for our plot

    plt.figure(figsize=(10, 5))

    #Loops through different assets to load its specific stock data

    for asset in assets:

        #Assigned variables are ran through the different defined functions

        data=load_data(asset)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)
        sharpe_ratio, annualised_volatility, max_drawdown=calculate_metrics(data)

        #Plots graph of drawdown against time
        
        plt.plot(data["Drawdown"], label=asset)

    #Adds legend, axis labels, title, gridlines to graph and returns the graph

    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Drawdown")
    plt.title("Drawdown Over Time")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    #Forms a list of colours to loop over for different colours of lines for different assets in the graph for strategy return values vs market return values

    colours=["blue", "orange", "green"]

    #Cycles i over the indexes formed by the function enumerate() so that each asset has a specific colour of line in the graph and cycles asset over the different assets in assets to plot the different return data for the different assets

    for i, asset in enumerate(assets):

        #Assigned variables are ran through the different defined functions

        data=load_data(asset)
        data=create_signals(data, short_window, long_window)
        data=backtesting(data)

        #Uses the value of i to assign the variable colour to the colour in colours at index i so its corresponding asset has the right colour line in the graph

        colour=colours[i]

        #Plots the strategy return values vs the market return values with the different assets with its corresponding colours and the market and strategy return values having different style of lines to be able to differentiate accordingly

        plt.plot(data["Cumulative_Market"], color=colour, linestyle="-", label=f"{asset}-Market")
        plt.plot(data["Cumulative_Strategy"], color=colour, linestyle="--", label=f"{asset}-Strategy")

    #Adds legend, axis labels, title, gridlines to graph and returns the graph

    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.title("Strategy Returns Vs Market Returns")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()