
import requests
from backend.tips import get_daily_tip


from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
def send_telegram_alert():
    quote, stock_tips = get_daily_tip()

    message = f"🌞 *Smart Invest Daily Tip*\n\n"               f"💬 *Quote of the Day:*\n_{quote}_\n\n"               f"📈 *Top Stocks (Past 5 Days)*\n{stock_tips}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=payload)
    return response.status_code, response.text
