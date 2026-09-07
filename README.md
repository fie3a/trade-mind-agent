# 🧠 Trading Mind Agent (AI Intelligence & Telegram Dispatcher)

> *An enterprise-grade, terminal-based AI market intelligence and risk assessment agent built for the Binance Agent OS Hackathon.*

---

## 🚀 Overview
Trading Mind Agent is a command-line interface (CLI) tool designed for crypto traders and developers. It hooks directly into live Binance market data streams via Python's standard libraries (urllib) to deliver deep technical sentiment analysis, automated risk management metrics, custom DCA (Dollar-Cost Averaging) simulations, and an instant Telegram Dispatcher for mobile alerts.

---

## ✨ Key Features

1. Live Market Intelligence:
   - Fetches 24-hour ticker data, price volatility spreads, and volume metrics directly from Binance public APIs.
2. AI Sentiment & Risk Assessment:
   - Automatically categorizes market behavior into Bullish, Bearish, or Neutral structures.
   - Computes dynamic Entry zones, Take Profit (TP), and Stop Loss (SL) targets.
3. Custom DCA Simulation Engine:
   - Interactive calculation module for tailored accumulation strategies (Daily, Weekly, Monthly) complete with projected portfolio ROI.
4. Telegram Alert Dispatcher :
   - Instantly dispatches comprehensive intelligence reports and DCA simulations directly to your Telegram chat or mobile device via secure runtime inputs (zero hardcoded credentials).
5. JSON Data Export:
   - Archives complete analysis sessions into structured local logs for backtesting and record-keeping.

---

## 🛠️ Technical Stack & Standards
- Language: Python 3.x (Pure standard library implementation: urllib, json, datetime, time, sys).
- Architecture: Lightweight, dependency-free CLI design ensuring cross-platform stability (Windows, macOS, Linux).
- Security: Runtime-only credential injection for Telegram Bot Tokens to guarantee 100% safety in public GitHub repositories.

---

## 📦 Installation & Quick Start

1. Clone the Repository:
   ```bash
   git clone https://github.com/fie3a/trade-mind-agent.git
   cd trading-mind-agent
   ```
2. Run the Agent
   ```bash
   python main.py
   ```
3. Interactive Flow:
​> Enter the target asset symbol (e.g., BTC, ETH).

​> Review the generated AI intelligence and risk report.

​> Configure your custom DCA strategy parameters.

​> Choose to export as a JSON log and/or dispatch the report directly to your Telegram bot in real-time.

## Hackathon Submission Details
Project: Binance Agent OS Hackathon

Developer: fie3a

Security Note: Designed with clean architecture, strict input validation loops, and absolute avoidance of hardcoded API secrets.
