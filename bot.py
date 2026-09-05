"*(Integration logic from your previous DCA project goes here)*\n\n"
        "Please use the format: /dca [amount_usd] [frequency]\n"
        "Example: /dca 50 weekly"
    )
    bot.reply_to(message, dca_info, parse_mode="Markdown")

# Run the bot
if __name__ == "__main__":
    print("[INFO] Trade Mind Agent (Analysis, Price & DCA) is running...")
    bot.infinity_polling()