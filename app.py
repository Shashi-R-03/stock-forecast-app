import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd

# Constants
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# App Title
st.title('📈 Stock Forecast App')

# User inputs
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

# Load stock data
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Load and display raw data
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('✅ Data loading complete!')

# Flatten multi-index columns if present
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

st.subheader('Raw data (tail)')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="Stock Open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Stock Close"))
    fig.layout.update(title_text='Time Series Data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Determine which price column to use: Prefer 'Close', else 'Adj Close'
price_col = None
if "Close" in data.columns:
    price_col = "Close"
elif "Adj Close" in data.columns:
    price_col = "Adj Close"
else:
    st.error("❌ Error: Neither 'Close' nor 'Adj Close' columns are found in the data.")

if price_col:
    # Prepare data for Prophet
    df_train = data[['Date', price_col]].copy()
    df_train = df_train.rename(columns={"Date": "ds", price_col: "y"})
    
    # Clean data: convert 'y' to numeric and drop non-numeric/missing values
    df_train.dropna(subset=["y"], inplace=True)
    df_train["y"] = pd.to_numeric(df_train["y"], errors="coerce")
    df_train.dropna(subset=["y"], inplace=True)
    
    
    # Validate cleaned data before fitting Prophet model
    if df_train.empty:
        st.error("❌ Error: The training dataset is empty after cleaning.")
    else:
        try:
            # Forecasting with Prophet
            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)
            
            # Display forecast
            st.subheader("Forecast data (tail)")
            st.write(forecast.tail())
            
            st.subheader(f'📊 Forecast plot for {n_years} year(s)')
            fig1 = plot_plotly(m, forecast)
            st.plotly_chart(fig1)
            
            st.subheader("📈 Forecast components")
            fig2 = m.plot_components(forecast)
            st.write(fig2)
            
        except Exception as e:
            st.error(f"❌ Prophet model fitting failed: {e}")
