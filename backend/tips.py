
import yfinance as yf
import datetime
import random

QUOTES_BY_DAY = {
    "Monday": "Start your week by investing in your future.",
    "Tuesday": "The earlier you invest, the greater the reward.",
    "Wednesday": "Midweek check-in: Stay committed to your financial goals!",
    "Thursday": "Think long-term. Invest smartly today.",
    "Friday": "Financial freedom begins with consistent action.",
    "Saturday": "Use weekends to review and rebalance your portfolio.",
    "Sunday": "Rest, reflect, and plan your financial week ahead.",
}

STOCK_TICKERS = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "BAJFINANCE.NS", "LT.NS", "SBIN.NS", "KOTAKBANK.NS", "BHARTIARTL.NS"
]

def fetch_high_return_stocks():
    stock_data = []
    for ticker in STOCK_TICKERS:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="5d")
            if len(hist) >= 2:
                pct_change = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
                stock_data.append({
                    "ticker": ticker.replace(".NS", ""),
                    "return": round(pct_change, 2)
                })
        except:
            continue

    stock_data.sort(key=lambda x: x["return"], reverse=True)
    return stock_data[:3]

def get_daily_tip():
    today = datetime.datetime.now().strftime("%A")
    quote = QUOTES_BY_DAY.get(today, "Keep investing wisely.")

    try:
        top_stocks = fetch_high_return_stocks()
        tips = "\n".join([f"📈 {s['ticker']} – {s['return']}% (past 5 days)" for s in top_stocks])
    except Exception as e:
        tips = f"❌ Could not fetch stock data: {e}"

    return quote, tips
