# Stock Price Visualizer 📈

A real-time stock price dashboard built with Python, Flask, and Plotly. 
Deployed on cloud using Docker and GitHub Actions CI/CD pipeline.

## 🔗 Live Demo
[https://stock-visualizer-3op7.onrender.com](https://stock-visualizer-3op7.onrender.com)

## 📊 Features
- Real-time stock data using Yahoo Finance API
- 4 interactive charts:
  - Candlestick chart (Open, High, Low, Close)
  - Closing price trend (Line chart)
  - Trading volume (Bar chart)
  - 20-day Moving Average
- Search any stock ticker (AAPL, TSLA, MSFT, INFY, TCS)
- Select time period (1 month to 2 years)

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Flask | Web framework |
| Pandas | Data processing |
| Plotly | Interactive charts |
| yfinance | Fetch real-time stock data |
| Docker | Containerisation |
| GitHub Actions | CI/CD pipeline |
| Render.com | Cloud deployment |

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/YukthaAM/stock-visualizer.git
cd stock-visualizer
```

**Step 2 — Create virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Run the app**
```bash
python app.py
```

**Step 5 — Open in browser**