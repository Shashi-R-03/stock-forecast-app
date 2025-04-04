# Stock Forecast App

This project is a web-based stock forecasting tool built with [Streamlit](https://streamlit.io) that allows users to select a stock, fetch historical data from Yahoo Finance using [yfinance](https://pypi.org/project/yfinance/), and forecast future stock prices using [Facebook Prophet](https://facebook.github.io/prophet/). Interactive visualizations are created with [Plotly](https://plotly.com) and data manipulation is handled by [pandas](https://pandas.pydata.org).

![App Preview](assets/preview.png)

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Execution](#execution)
- [Usage](#usage)
- [Notes](#notes)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)

---

## Features

- **Real-time Data Fetching:** Retrieves historical stock data from Yahoo Finance.
- **Interactive Stock Selection:** Choose from a set list of stocks (GOOG, AAPL, MSFT, GME).
- **Customizable Forecasting:** Adjust the forecast period (1 to 4 years) with an interactive slider.
- **Data Visualization:** Displays historical data and forecast plots using Plotly.
- **Forecasting with Prophet:** Uses Facebook Prophet to model and predict future stock prices.
- **Component Analysis:** Decomposes forecast data to show trends and seasonality.
- **Data Caching:** Caches data with Streamlit's `@st.cache_data` decorator for improved performance.

---

## Technologies Used

| Library/Tool  | Purpose                                       | Link                                                             |
|---------------|-----------------------------------------------|------------------------------------------------------------------|
| Streamlit     | Web application framework                     | [streamlit.io](https://streamlit.io)                              |
| yfinance      | Fetching stock data                           | [yfinance on PyPI](https://pypi.org/project/yfinance/)            |
| Prophet       | Time series forecasting                       | [Facebook Prophet](https://facebook.github.io/prophet/)            |
| Plotly        | Interactive visualizations                    | [plotly.com](https://plotly.com)                                  |
| pandas        | Data manipulation and analysis                | [pandas.pydata.org](https://pandas.pydata.org)                    |

---

## Project Structure

```plaintext
stock-forecast-app/
│
├── app.py                # Main application script containing the Streamlit app code
├── README.md             # This file
├── requirements.txt      # List of project dependencies
└── assets/
    └── preview.png       # App preview image (optional)
```

# Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/Shashi-R-03/stock-forecast-app.git
cd stock-forecast-app
```

## Step 2: Install Dependencies
Install the required packages using requirements.txt:
```bash
pip install -r requirements.txt
```
Alternatively, you can install the dependencies manually:
```bash
pip install streamlit yfinance prophet plotly pandas
```
Note: If you encounter issues installing Prophet, please refer to the Prophet installation guide.

# Execution
To run the application, execute the following command:
```bash
streamlit run app.py
```
This will launch the app in your default web browser.

# Usage
## Select Stock:
#### Use the dropdown to choose a stock from the available options (GOOG, AAPL, MSFT, GME).
### Set Forecast Period:
#### Adjust the slider to select the number of years (1-4) for forecasting.
### View Historical Data:
#### The app fetches and displays historical stock data starting from January 1, 2015.
### Visualize Data:
#### View interactive plots showing the stock's "Open" and "Close" prices with a range slider for detailed exploration.
### Forecast Future Prices:
#### The app processes and cleans the data, then uses Prophet to generate and display a forecast plot along with its components (trend and seasonality).

# Notes
### Data Caching:
#### Data is cached using the @st.cache_data decorator to enhance performance.
### Prophet Requirements:
#### Prophet expects the input DataFrame to have columns ds (date) and y (numeric value). The code renames the Date column to ds and the price column (Close or Adj Close) to y.
### Error Handling:
#### The app includes error handling to manage issues such as missing columns or an empty dataset after cleaning.

# Troubleshooting
### Empty Dataset Error:
#### If you encounter the error "The training dataset is empty after cleaning," verify that the selected stock has valid closing price data.
### Prophet Model Fitting Error:
#### If the Prophet model fails to fit, check for non-numeric or missing values in the dataset and ensure the data format meets Prophet's requirements.

# Future Enhancements
#### Allow users to input custom stock tickers beyond the predefined list.
#### Include additional metrics such as Volume, High, and Low prices.
#### Provide an option to export forecast data as CSV.
#### Deploy the app using Streamlit Cloud.






