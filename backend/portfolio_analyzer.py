
import pandas as pd
import yfinance as yf

def analyze_portfolio(csv_file):
    try:
        df = pd.read_csv(csv_file)

        if "Asset" not in df.columns or "Quantity" not in df.columns:
            return None, "❌ CSV must have 'Asset' and 'Quantity' columns."

        prices = []
        values = []

        for index, row in df.iterrows():
            ticker = row['Asset']
            qty = row['Quantity']
            try:
                stock = yf.Ticker(ticker + ".NS")
                live_price = stock.history(period="1d")['Close'].iloc[-1]
                prices.append(live_price)
                values.append(live_price * qty)
            except Exception:
                prices.append(0)
                values.append(0)

        df['Live Price (₹)'] = prices
        df['Total Value (₹)'] = values

        total = df['Total Value (₹)'].sum()
        df['Weight (%)'] = round((df['Total Value (₹)'] / total) * 100, 2)

        tips = []
        if df['Weight (%)'].max() > 50:
            tips.append("⚠️ Consider reducing concentration in one asset.")
        if len(df) < 4:
            tips.append("⚠️ Add more assets for diversification.")

        return df, "\n".join(tips) if tips else "✅ Portfolio is balanced and diversified."
    except Exception as e:
        return None, f"❌ Error: {e}"
