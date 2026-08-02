from flask import Flask, render_template
import json
import plotly
import plotly.express as px
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    df = yf.download(tickers, period='1y')
    close_df = df['Close'].reset_index()
    melted = close_df.melt(id_vars='Date', var_name='Ticker', value_name='Close')
    fig = px.line(melted, x='Date', y='Close',
                  color='Ticker', title='Tech Stocks 2024-2025')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

@app.route('/summary')
def summary():
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    summary_data = []
    for ticker in tickers:
        df = yf.download(ticker, period='1y')
        summary_data.append({
            'Ticker': ticker,
            'Current Price': round(df['Close'][ticker].iloc[-1], 2),
            'Max Price': round(df['Close'][ticker].max(), 2),
            'Min Price': round(df['Close'][ticker].min(), 2)
        })
    df_summary = pd.DataFrame(summary_data)
    return df_summary.to_html()

if __name__ == "__main__":
    app.run(debug=True, port=8050)