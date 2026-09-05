import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    try:
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print(f"[ERROR] Gagal koneksi ke Telegram: {e}")
        return None

# Fungsi diperbarui agar bisa menerima tombol interaktif (reply_markup)
def send_message(chat_id, text, reply_markup=None):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": text, 
        "parse_mode": "Markdown"
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(url, json=payload)

def main():
    print("[INFO] Trade Mind Agent sedang berjalan di Terminal...")
    print("[INFO] Menunggu perintah dari Telegram (Tekan Ctrl+C untuk berhenti)...")
    
    last_update_id = None
    
    while True:
        updates = get_updates(offset=last_update_id)
        
        if updates and "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                
                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    user_message = update["message"]["text"]
                    user_name = update["message"]["from"].get("first_name", "User")
                    
                    print(f"[Pesan Diterima] Dari {user_name}: {user_message}")
                    
                    # Konfigurasi Tombol Menu Interaktif di Bawah Chat
                    keyboard_menu = {
                        "keyboard": [
                            [{"text": "/price"}, {"text": "/dca"}],
                            [{"text": "/tpsl"}, {"text": "/help"}]
                        ],
                        "resize_keyboard": True,
                        "one_time_keyboard": False
                    }
                    
                    # Logika Respon Perintah
                    if user_message.lower() == "/start":
                        reply_text = f"Hello *{user_name}*! Welcome to *Trade Mind Agent*.\n\nChoose a menu below or type a command to start:"
                        send_message(chat_id, reply_text, reply_markup=keyboard_menu)
                        
                    elif user_message.lower() == "/help":
                        reply_text = "🛠 *Available Commands*:\n/price - Check real-time coin price\n/dca - Run DCA simulation\n/tpsl - Calculate TP/SL targets"
                        send_message(chat_id, reply_text, reply_markup=keyboard_menu)
                        
                    elif user_message.lower() == "/price":
                        reply_text = "📊 *Price Tracker*: Feature under development. Will integrate Binance API soon!"
                        send_message(chat_id, reply_text, reply_markup=keyboard_menu)
                        
                    elif user_message.lower() == "/dca":
                        reply_text = "📈 *DCA Simulator*: Feature under development."
                        send_message(chat_id, reply_text, reply_markup=keyboard_menu)
                        
                    elif user_message.lower() == "/tpsl":
                        reply_text = "📐 *TP/SL Calculator*: Feature under development."
                        send_message(chat_id, reply_text, reply_markup=keyboard_menu)
                        
                    else:
                        reply_text = f"Unknown command: {user_message}. Type /help for assistance."
                        send_message(chat_id, reply_text, reply_markup=keyboard_menu)
                    
        time.sleep(1)

if __name__ == "__main__":
    main()
import os
import telebot
from dotenv import load_dotenv

# Load configuration from .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# 1. Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🤖 *Welcome to Trade Mind Agent!*\n\n"
        "Your intelligent assistant for market analysis & crypto DCA simulation.\n\n"
        "📋 *Main Menu:*\n"
        "🔍 /analyze [COIN_NAME] - Technical analysis, momentum, entry, TP/SL\n"
        "📊 /dca - Dollar-Cost Averaging simulation calculator\n"
        "💡 Type any command above to get started!"
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

# 2. Handler for Coin Analysis Feature
@bot.message_handler(commands=['analyze', 'analisis'])
def handle_analysis(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ Incorrect format. Example usage: /analyze BTC", parse_mode="Markdown")
        return
    
    coin = args[1].upper()
    
    # [You can integrate real market API logic here]
    analysis_result = (
        f"🔍 *Technical Analysis Report: {coin}/USDT*\n\n"
        f"📈 *Market Trend:* Bullish Moderate\n"
        f"⚡ *Momentum:* Accumulation / Volume increasing\n"
        f"🎯 *Suggested Entry:* Near support zones\n"
        f"🟢 *Take Profit (TP):* Resistance levels 1 & 2\n"
        f"🔴 *Stop Loss (SL):* Below minor support\n\n"
        f"_Disclaimer: Always manage your risk wisely!_"
    )
    bot.reply_to(message, analysis_result, parse_mode="Markdown")

# 3. Handler for DCA Simulation Feature
@bot.message_handler(commands=['dca'])
def handle_dca(message):
    dca_info = (
        "📊 *DCA Simulation Calculator*\n\n"
        "This feature helps you calculate regular crypto accumulation.\n"
        "*(Integration logic from your previous DCA project goes here)*\n\n"
        "Please use the format: /dca [amount_usd] [frequency]\n"
        "Example: /dca 50 weekly"
    )
    bot.reply_to(message, dca_info, parse_mode="Markdown")

# Run the bot
if __name__ == "__main__":
    print("[INFO] Trade Mind Agent (Analysis & DCA) is running...")
    bot.infinity_polling()