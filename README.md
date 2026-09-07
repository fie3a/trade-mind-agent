# 🤖• Trading Mind Agent

> AI Market Intelligence & Telegram Dispatcher Matrix.

---

## 🚀 Overview
• Trading Mind Agent is an advanced, lightweight Streamlit-based dashboard designed to fetch real-time crypto market data (via Binance & CoinGecko APIs), calculate technical indicators and optimal DCA (Dollar-Cost Averaging) simulations, and instantly dispatch structured strategy alerts to Telegram bots or channels.

---

## ✨ Key Features
- Real-Time Price Feeds: Multi-endpoint fallback architecture ensuring reliable live asset pricing (BTC, ETH, SOL, BNB, etc.).
- Custom Neon SVG Charts: High-performance, responsive price trend visualization styled with sleek cyberpunk aesthetics.
- Automated DCA Calculator: Comprehensive simulation tracking periodic capital commitment, duration cycles, and estimated asset accumulation.
- Telegram Dispatcher Matrix: One-click automated formatting and transmission of actionable trading signals (Entry, TP, SL, and DCA plans) directly via Telegram Bot API.

---

## 🛠️ Tech Stack
- Frontend / Dashboard: [Streamlit](https://streamlit.io/) & Custom HTML/SVG components.
- Data Sources: Binance REST API & CoinGecko API.
- Notifications: Telegram Bot API (requests / urllib).
- Language: Python 3.10+

---

## ⚙️ Quick Start / Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fie3a/trade-mind-agent.git
   cd trade-mind-agent
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```
   
 ## 📲 How to Use
1. Enter your target trading pair (e.g., BTCUSDT, ETHUSDT, BNBUSDT) in the sidebar.
2. Set your DCA parameters (amount, interval type, cycles) and analysis timeframe.
3. Input your Telegram Bot Token and Chat ID (optional, for live signal pushing).
4. Click "Run Analysis & Push to Telegram" to generate live metrics, charts, and automated dispatch logs.
