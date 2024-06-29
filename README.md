# Stock Price Prediction Application

A web-based application built with Streamlit for predicting stock prices using the SARIMAX model from the `statsmodels` library. This project utilizes historical stock data to forecast future prices for major companies like Google, Apple, Microsoft, and Amazon.

## Overview

This application allows users to select a stock and a period of historical data to train a SARIMAX model. After training, the model predicts future stock prices and visualizes the actual versus predicted prices.

### Key Features

- **User-friendly Interface**: Easy-to-use Streamlit interface for selecting stocks and training periods.
- **Data Visualization**: Interactive visualizations using Plotly for analyzing stock price trends.
- **Forecasting**: Predict future stock prices using the SARIMAX model.
- **Caching**: Efficient data loading with Streamlit's caching mechanism.
## Requirements

- Python 3.x
- Streamlit
- Plotly
- yfinance
- statsmodels
- pandas

## Installation

1. **Clone the repository**:

``` 
git clone xxxx cd stock-price-prediction-app
```

2. **Create and activate a virtual environment**:

```
python3 -m venv venv source venv/bin/activate  # On Windows use venv\Scripts\activate 
```
3. **Install the required dependencies**:

```
pip install -r requirements.txt
```
## Usage

1. **Run the application**:

```
streamlit run main.py
```

2. **Open your web browser** and go to `http://localhost:8501`.
    
3. **Interact with the application**:
    
    - Select a stock from the dropdown menu.
    - Choose the number of years of historical data for training the model.
    - View raw data and visualizations.
    - Train the model and see the prediction results.

## File Structure

`stock-price-prediction-app/ │ ├── main.py ├── requirements.txt ├── README.md ├── .gitignore`

- `main.py`: Main application file containing the Streamlit app code.
- `requirements.txt`: List of Python dependencies required for the project.
- `README.md`: Project documentation.


## Acknowledgements

- **Streamlit**: For providing a powerful framework for creating interactive web applications.
- **Plotly**: For offering versatile and interactive plotting tools.
- **yfinance**: For enabling easy access to historical stock data.
- **statsmodels**: For providing robust statistical modeling tools.
