
import streamlit as st
from backend.chatbot import gemini_chat
from backend.portfolio_analyzer import analyze_portfolio
from backend.tips import get_daily_tip

st.set_page_config(page_title="Smart Invest", layout="wide")
st.title("📈 Smart Invest – Your AI Investment Assistant")

tab1, tab2, tab3 = st.tabs(["💬 Investment Chatbot", "📊 Portfolio Analyzer", "💡 Daily Investment Tips"])

# Tab 1 - Gemini Investment Chatbot
with tab1:
    st.subheader("AI-Powered Investment Planning")
    user_input = st.text_area("💬 Ask anything about investing, risk, or return strategy:")
    if st.button("Get AI Suggestion"):
        if user_input:
            with st.spinner("Thinking..."):
                response = gemini_chat(user_input)
                st.success("✅ Gemini's Investment Insight:")
                st.write(response)
        else:
            st.warning("Please enter a prompt to continue.")

# Tab 2 - Portfolio Analyzer
with tab2:
    st.subheader("📊 Analyze Your Portfolio (Live Prices)")
    uploaded_file = st.file_uploader("Upload your portfolio CSV (columns: Asset, Quantity)", type=["csv"])
    if uploaded_file:
        df, analysis = analyze_portfolio(uploaded_file)
        st.dataframe(df)
        st.success("📌 Analysis & Suggestions")
        st.write(analysis)

# Tab 3 - Real-Time Investment Tips
with tab3:
    st.subheader("📅 Smart Daily Investment Insights")
    quote, stock_tips = get_daily_tip()

    st.markdown("### 💬 Quote of the Day")
    st.info(quote)

    st.markdown("### 📈 Top Performing Stocks (Past 5 Days)")
    st.success(stock_tips)
