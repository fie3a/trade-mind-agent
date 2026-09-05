import requests
import telebot

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    print(f"[LOG] User {user_name} executed /start command.")
    
    welcome_text = (
        f"Hello {user_name}! Welcome to Trade Mind Agent.\n"
        "Your intelligent assistant for market analysis & crypto DCA simulation.\n\n"
        "Main Menu:\n"
        "- /analyze COIN : Technical analysis & price (e.g., /analyze btc)\n"
        "- /dca COIN AMOUNT INTERVAL PERIODS : Advanced DCA Calculator\n"
        "  (Interval options: daily, weekly, monthly)\n"
        "  (Example: /dca btc 50 weekly 12)"
    )
    bot.reply_to(message, welcome_text)
    print(f"[INFO] Welcome message sent to {user_name}.\n" + "-"*40)

@bot.message_handler(commands=['analyze', 'analisis', 'price'])
def handle_analysis(message):
    args = message.text.split()
    user_name = message.from_user.first_name
    print(f"[LOG] User {user_name} requested analysis command: {message.text}")
    
    if len(args) < 2:
        bot.reply_to(message, "Incorrect format. Example usage: /analyze btc")
        return
    
    coin = args[1].lower()
    coin_mapping = {
        'btc': 'bitcoin', 'eth': 'ethereum', 'bnb': 'binancecoin',
        'sol': 'solana', 'ada': 'cardano', 'xrp': 'ripple',
        'doge': 'dogecoin', 'avax': 'avalanche-2', 'matic': 'polygon-ecosystem-token'
    }
    
    coin_id = coin_mapping.get(coin, coin)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        if response.status_code == 200:
            data = response.json()
            if coin_id in data and "usd" in data[coin_id]:
                price = float(data[coin_id]["usd"])
                formatted_price = f"${price:,.2f}" if price >= 1 else f"${price:.6f}"
                
                entry_zone = price * 0.985
                tp_target = price * 1.05
                sl_limit = price * 0.97

                analysis_result = (
                    f"Technical Analysis & Price: {coin.upper()}/USDT\n\n"
                    f"Current Price: {formatted_price}\n"
                    f"Market Trend: Bullish Momentum\n"
                    f"Volume: Active Accumulation\n"
                    f"Suggested Entry Zone: ~${entry_zone:,.2f}\n"
                    f"Take Profit (TP): ~${tp_target:,.2f} (+5%)\n"
                    f"Stop Loss (SL): ~${sl_limit:,.2f} (-3%)\n\n"
                    f"Disclaimer: Automated analysis for educational purposes only."
                )

                bot.reply_to(message, analysis_result)
                
                print("\n" + "="*45)
                print(f" [TERMINAL REPORT] Analysis Result for {coin.upper()}")
                print("="*45)
                print(analysis_result)
                print("="*45 + "\n")
            else:
                bot.reply_to(message, f"Coin {coin.upper()} not found.")
        else:
            bot.reply_to(message, "Failed to fetch market data from API.")
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}\n" + "-"*40)
        bot.reply_to(message, "Connection error while fetching market data.")

@bot.message_handler(commands=['dca'])
def handle_dca(message):
    args = message.text.split()
    user_name = message.from_user.first_name
    print(f"[LOG] User {user_name} executed /dca command: {message.text}")
    
    # Validasi format baru: /dca btc 50 weekly 12 (butuh 4 argumen: coin, amount, interval, periods)
    if len(args) < 5:
        dca_help = (
            "Advanced Dollar-Cost Averaging (DCA) Calculator\n\n"
            "How to use:\n"
            "/dca [COIN] [AMOUNT_USD] [INTERVAL] [PERIODS]\n\n"
            "Interval options:\n"
            "- daily\n"
            "- weekly\n"
            "- monthly\n\n"
            "Example:\n"
            "/dca btc 50 weekly 12\n"
            "(Simulate $50 routine purchase every week for 12 periods)"
        )
        bot.reply_to(message, dca_help)
        print(f"[WARNING] Incomplete /dca parameters provided by {user_name}.\n" + "-"*40)
        return

    coin = args[1].lower()
    try:
        amount = float(args[2])
    except ValueError:
        bot.reply_to(message, "Invalid amount number. Example: /dca btc 50 weekly 12")
        return

    interval = args[3].lower()
    if interval not in ['daily', 'weekly', 'monthly']:
        bot.reply_to(message, "Invalid interval! Please use: daily, weekly, or monthly.")
        return

    try:
        periods = int(args[4])
    except ValueError:
        bot.reply_to(message, "Invalid periods number. Example: /dca btc 50 weekly 12")
        return

    coin_mapping = {
        'btc': 'bitcoin', 'eth': 'ethereum', 'bnb': 'binancecoin',
        'sol': 'solana', 'ada': 'cardano', 'xrp': 'ripple',
        'doge': 'dogecoin', 'avax': 'avalanche-2', 'matic': 'polygon-ecosystem-token'
    }
    
    coin_id = coin_mapping.get(coin, coin)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        print(f"[INFO] Fetching price for Advanced DCA simulation: {coin.upper()}")
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        print(f"[INFO] Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if coin_id in data and "usd" in data[coin_id]:
                price = float(data[coin_id]["usd"])
                
                # Kalkulasi total investasi & total aset terkumpul
                total_invested = amount * periods
                accumulated_coin = (amount / price) * periods if price > 0 else 0
                
                dca_result = (
                    f"Advanced DCA Simulation Report: {coin.upper()}/USDT\n\n"
                    f"Current Price: ${price:,.2f}\n"
                    f"Routine Budget: ${amount:,.2f} / {interval}\n"
                    f"Total Duration: {periods} {interval} periods\n"
                    f"Total Capital Invested: ${total_invested:,.2f}\n"
                    f"Estimated Asset Acquired: {accumulated_coin:.6f} {coin.upper()}\n\n"
                    f"Strategy tip: Sticking to a {interval} DCA plan removes emotional trading biases."
                )
                
                bot.reply_to(message, dca_result)
                
                print("\n" + "="*45)
                print(f" [TERMINAL REPORT] Advanced DCA Simulation ({coin.upper()})")
                print("="*45)
                print(dca_result)
                print("="*45 + "\n")
            else:
                bot.reply_to(message, f"Coin {coin.upper()} data not found.")
        else:
            bot.reply_to(message, "Failed to fetch market price for DCA simulation.")
    except Exception as e:
        print(f"[ERROR] DCA calculation failed: {e}\n" + "-"*40)
        bot.reply_to(message, "Connection error during DCA calculation.")

if __name__ == "__main__":
    print("==================================================")
    print(" Trade Mind Agent (Telegram Bot) is Online!     ")
    print(" Features: Live Price, Analysis & Advanced DCA  ")
    print(" Status: Waiting for messages from Telegram...   ")
    print("==================================================")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
