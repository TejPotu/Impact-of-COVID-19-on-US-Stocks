import yfinance as yf
import pandas as pd

# Define the ticker symbols
tickers = ["SNAP", "AMZN", "INTC", "MSFT", "META", "TWTR", "GOOG", "ZM", "AAPL"]

# Define the start and end dates for the data
start_date = "2020-01-01"
end_date = "2023-03-30"

# Download the stock data for each ticker and store it in a dictionary
stock_data = {}
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date, interval='1wk')
    stock_data[ticker] = data

# Save the data for each ticker in a separate CSV file
for ticker, data in stock_data.items():
    data.to_csv(f"{ticker}.csv")
