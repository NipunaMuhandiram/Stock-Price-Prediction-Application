
import streamlit as st
from datetime import date
import plotly.express as px 
import yfinance as yf
from plotly import graph_objs as go
import statsmodels.api as sm
import pandas as pd

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.divider() 
st.title(':rainbow[STOCK Price Prediction Application]')
st.divider() 

stocks = ('GOOG', 'AAPL', 'MSFT', 'AMZN')
st.write("###### GOOG - GOOGLE STOCKS / AAPL - APPLE STOCKS / MSFT - Microsoft STOCKS / AMZN - Amazon.com STOCKS")
selected_stock = st.selectbox('Select STOCK dataset you want to predict', stocks)
st.text("You can select 4-years max of STOCK data to train the Machine Learning Model ")
n_years = st.slider('Years of Dataset to Train Model:', 1, 4)
period = n_years * 365

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw STOCK data', divider='rainbow')
st.success("###### Open - the first traded price.")
st.success('###### High - the highest traded price.')
st.success('###### Low - the lowest traded price.')
st.success('###### Close - the final traded price.')
st.success('###### Volume - the total volume traded by all trades')
st.write(data)

# Visualize raw data
st.header('Raw Data Visualize', divider='rainbow')
fig = px.line(data, x='Date', y='Close', title='Closing Price of Stock', width=1000, height=600)
st.plotly_chart(fig)

# Select column to forecast
column = 'Close'
data = data[['Date', column]]

# SARIMAX model parameters
p, d, q = 1, 1, 2
seasonal_order = 12

# Train the model
data_load_state = st.text('Training SRIMAX Forecasting Model Please wait...')
model = sm.tsa.statespace.SARIMAX(data[column], order=(p, d, q), seasonal_order=(p, d, q, seasonal_order))
model = model.fit()

st.header('Model Summary')
st.write(model.summary())
data_load_state.text('Model training is done!... and good to make predictions')

# Model Prediction
st.header('Model Prediction', divider='rainbow')
forecast_period = 10

predictions = model.get_prediction(start=len(data), end=len(data) + forecast_period - 1)
predictions = predictions.predicted_mean
predictions.index = pd.date_range(start=TODAY, periods=len(predictions), freq='D')
predictions = pd.DataFrame(predictions, columns=['predicted_mean'])
predictions.insert(0, 'Date', predictions.index, True)
predictions.reset_index(drop=True, inplace=True)

# Plot Actual vs Predicted
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['Date'], y=data[column], mode='lines', name='Actual', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=predictions['Date'], y=predictions['predicted_mean'], mode='lines', name='Predicted', line=dict(color='red')))
fig.update_layout(title='Actual vs Predicted STOCK Prices', xaxis_title='Date', yaxis_title='Price', width=900, height=400)
st.plotly_chart(fig)
