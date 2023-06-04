#%% 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def get_stock_data(symbol, start_date, end_date):
    stock = yf.download(symbol, start=start_date, end=end_date)
    return stock

def plot_stock_prices(data, symbol):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], color='blue', label='Stock Price')
    plt.title(f"Stock Prices for {symbol}")
    plt.xlabel('Date')
    plt.ylabel('Price')

    # Add data labels for min, max, last, and slope values
    min_price = data['Close'].min()
    max_price = data['Close'].max()
    last_price = data['Close'].iloc[-1]
    min_date = data['Close'].idxmin().strftime('%Y-%m-%d')
    max_date = data['Close'].idxmax().strftime('%Y-%m-%d')
    last_date = data.index[-1].strftime('%Y-%m-%d')

    plt.text(data.index[0], min_price, f"Min: {min_price:.2f}", fontsize=10, va='bottom')
    plt.text(data.index[0], max_price, f"Max: {max_price:.2f}", fontsize=10, va='top')
    plt.text(data.index[-1], last_price, f"Last: {last_price:.2f}", fontsize=10, va='bottom')

    # Add trend line
    x = data.index.to_pydatetime()  # Use actual dates as x values
    y = data['Close'].values
    slope, intercept = np.polyfit(x, y, 1)
    trendline = intercept + slope * x
    plt.plot(data.index, trendline, color='red', linestyle='--', label='Trend Line')

    # Add data label for slope
    slope_label = f"Slope: {slope:.2f}"
    plt.text(data.index[int(len(data)/2)], data['Close'].iloc[int(len(data)/2)], slope_label,
             fontsize=10, va='top', color='red')

    plt.legend()
    plt.show()

def calculate_returns(data):
    data['Return'] = data['Close'].pct_change()
    return data

def analyze_stocks(stocks, start_date, end_date):
    for symbol in stocks:
        try:
            data = get_stock_data(symbol, start_date, end_date)
            plot_stock_prices(data, symbol)
            data_with_returns = calculate_returns(data)
            print(f"Returns for {symbol}:")
            print(data_with_returns['Return'])
            print()
        except Exception as e:
            print(f"Error analyzing stock {symbol}: {str(e)}")

# Prompt the user to enter stock symbols
stocks_input = input("Enter stock symbols (comma-separated): ")
stocks = [symbol.strip() for symbol in stocks_input.split(",")]

# Define the start date and set the end date to today
start_date = '2022-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

# Analyze the stocks
analyze_stocks(stocks, start_date, end_date)

# %%
