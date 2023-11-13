from flask import Flask, render_template, request
import pyodbc
import yfinance as yf
import pandas as pd

app = Flask(__name__)

connectionserver = 'localhost\\SQLEXPRESS'
database = 'project'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rundate', methods=['POST'])
def run_date():
    selected_date = request.form.get('selectDate')
    
    # Database connection
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={connectionserver};DATABASE={database};')
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM data")
    results = cursor.fetchall()

    stock_symbols = [row[1] for row in results]
    stock_prices = {}

    for stock_symbol in stock_symbols:
        ticker_data = yf.Ticker(stock_symbol)
        
        # Retrieve historical data for a range of dates, for example, 7 days prior to the selected date
        start_date = (pd.to_datetime(selected_date) - pd.DateOffset(days=1)).strftime('%Y-%m-%d')
        end_date = selected_date
        ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

        if not ticker_df.empty:
            stock_prices[stock_symbol] = ticker_df[['Close']].to_dict(orient='records')
        else:
            stock_prices[stock_symbol] = None

    conn.close()

    return render_template('index.html', stock_prices=stock_prices, results=results, selected_date=selected_date)

if __name__ == '__main__':
    app.run(debug=True)