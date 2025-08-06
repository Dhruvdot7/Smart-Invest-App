
import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def gemini_chat(prompt: str) -> str:
    investment_prompt = f"""You are a financial advisor. 
    The user asked: "{prompt}" 
    Give a complete investment plan considering return, risk levels (low/medium/high), time horizon, and diversification."""

    try:
        response = model.generate_content(investment_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"
