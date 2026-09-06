# Trade Mind Agent 🤖📈

Trade Mind Agent is an intelligent, lightweight Telegram bot designed for real-time cryptocurrency price tracking, automated technical analysis (with Entry, TP, and SL targets), and advanced Dollar-Cost Averaging (DCA) simulation. 

Built with Python and powered by real-time market data APIs, this bot helps traders quickly simulate investment strategies and track momentum directly from their Telegram chat.

---

## 🚀 Key Features

* **Real-Time Price & Analysis (/analyze):** Fetches live coin prices from market data providers and instantly calculates recommended Entry Zones, Take Profit (TP), and Stop Loss (SL) targets.
* **Advanced DCA Simulation (/dca):** Simulates routine investments with customizable intervals (daily, weekly, monthly) and specified duration periods to calculate total capital and estimated asset acquisition.
* **Terminal Logging & Monitoring:** Mirrors bot activity and outputs detailed real-time logs directly to the local terminal/CMD for easy tracking.
* **Robust Network Stability:** Built-in connection error handling, custom timeouts, and secure request verification for smooth performance.

---

## 🛠️ Tech Stack

* Language: Python 3.x
* Libraries: pyTelegramBotAPI, requests, urllib3
* API: CoinGecko Market API

---

## 📋 Commands List

| Command | Description | Example |
| :--- | :--- | :--- |
| /start | Start the bot and view greeting menu | /start |
| /analyze | Run technical analysis and check live price | /analyze btc |
| /dca | Run advanced DCA simulation with intervals | /dca btc 50 weekly 12 |

---

## ⚙️ Installation & Setup (Local)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/fie3a/trade-mind-agent.git
   cd trade-mind-agent
```
```
2. Install required dependencies :
   ```bash
   pip install pyTelegramBotAPI requests urllib3
   ```
3. Configure your Bot Token:
Open bot.py and replace the TOKEN variable with your unique Telegram Bot Token from @BotFather.

4. Run the bot
   ```bash
   python bot.py
   ```
## 📄 License

© 2026 Trade Mind Agent. All rights reserved.

This project is developed for educational and portfolio demonstration purposes.

