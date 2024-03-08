import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbols
#tickers = ["WBA", "CAH", "CVS", "ABC", "CNC", "PFE", "BNTX","UNH", "CI", "JNJ"]

tickers = ["PFE"]
# Define the start and end dates for the data
start_date = "2019-01-01"
end_date = "2022-03-30"

# Download the stock data for each ticker and store it in a dictionary
stock_data = {}
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date, interval='1wk')
    stock_data[ticker] = data
# Plot the closing prices for each ticker
plt.figure(figsize=(10, 6))
for ticker, data in stock_data.items():
    plt.plot(data.index, data["Close"], label=ticker)

# Add labels and legend to the plot
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Prices during COVID Period")
plt.legend()

# Display the plot
plt.show()

'''
# Save the data for each ticker in a separate CSV file
for ticker, data in stock_data.items():
    data.to_csv(f"{ticker}.csv")
'''