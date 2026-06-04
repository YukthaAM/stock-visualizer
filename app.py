from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objects as go
import plotly.utils
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ticker = "AAPL"
    period = "6mo"
    error = None

    if request.method == "POST":
        ticker = request.form.get("ticker", "AAPL").upper()
        period = request.form.get("period", "6mo")

    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)

        if df.empty:
            error = f"No data found for ticker '{ticker}'. Please try another."
            return render_template("index.html", charts=[], ticker=ticker,
                                   period=period, company_name=ticker,
                                   current_price="N/A", error=error)

        # Chart 1: Candlestick
        fig1 = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df["Open"], high=df["High"],
            low=df["Low"], close=df["Close"],
            name=ticker
        )])
        fig1.update_layout(title=f"{ticker} Price (Candlestick)",
                           xaxis_title="Date", yaxis_title="Price (USD)")

        # Chart 2: Closing price
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df.index, y=df["Close"],
                                  mode="lines", name="Close Price",
                                  line=dict(color="royalblue")))
        fig2.update_layout(title=f"{ticker} Closing Price Trend",
                           xaxis_title="Date", yaxis_title="Price (USD)")

        # Chart 3: Volume
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=df.index, y=df["Volume"],
                              name="Volume", marker_color="orange"))
        fig3.update_layout(title=f"{ticker} Trading Volume",
                           xaxis_title="Date", yaxis_title="Volume")

        # Chart 4: Moving average
        df["MA20"] = df["Close"].rolling(window=20).mean()
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(x=df.index, y=df["Close"],
                                  mode="lines", name="Close",
                                  line=dict(color="blue")))
        fig4.add_trace(go.Scatter(x=df.index, y=df["MA20"],
                                  mode="lines", name="20-day MA",
                                  line=dict(color="red", dash="dash")))
        fig4.update_layout(title=f"{ticker} Moving Average (20-day)",
                           xaxis_title="Date", yaxis_title="Price (USD)")

        charts = [
            json.dumps(fig.to_dict(), cls=plotly.utils.PlotlyJSONEncoder)
            for fig in [fig1, fig2, fig3, fig4]
        ]

        try:
            info = stock.info
            company_name = info.get("longName", ticker)
            current_price = info.get("currentPrice", "N/A")
        except:
            company_name = ticker
            current_price = "N/A"

        return render_template("index.html",
                               charts=charts,
                               ticker=ticker,
                               period=period,
                               company_name=company_name,
                               current_price=current_price,
                               error=None)

    except Exception as e:
        error = f"Could not fetch data for '{ticker}'. Please try again."
        return render_template("index.html", charts=[], ticker=ticker,
                               period=period, company_name=ticker,
                               current_price="N/A", error=error)

if __name__ == "__main__":
    app.run(debug=True)