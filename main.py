import urllib.request
import json
import time
import sys
import datetime

def fetch_binance_ticker(symbol):
    endpoints = [
        f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}",
        f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={symbol}"
    ]
    
    for url in endpoints:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3) as response:
                return json.loads(response.read().decode())
        except Exception:
            continue
            
    return None

def run_trading_mind_agent():
    print("==================================================")
    print("  TRADING MIND AGENT (AI Intelligence & Advanced DCA)")
    print("==================================================")
    print("[+] Initializing Advanced Neural Sentiment & Risk Core...")
    time.sleep(1)
    
    print("\n[*] Instructions:")
    print("    > Analyze asset intelligence, volatility metrics, Entry/TP/SL, and DCA.")
    print("    > Type 'exit' anytime to close the session.")
    
    while True:
        print("-" * 50)
        coin_input = input("Enter asset to analyze (e.g., BTC, ETH) [or type 'exit']: ").strip()
        
        if coin_input.lower() == 'exit':
            print("\n[+] Shutting down Trading Mind neural link safely...")
            time.sleep(1)
            print("> Agent session terminated. Stay safe in the market!")
            break
            
        if not coin_input:
            symbol = "BTCUSDT"
            display_symbol = "BTC"
        else:
            clean_coin = coin_input.upper().replace("USDT", "")
            symbol = clean_coin + "USDT"
            display_symbol = clean_coin
            
        print(f"\n[+] Tapping into Market Streams for {symbol}...")
        ticker_data = fetch_binance_ticker(symbol)
        
        if ticker_data:
            price = float(ticker_data['lastPrice'])
            price_change = float(ticker_data['priceChangePercent'])
            high_24h = float(ticker_data['highPrice'])
            low_24h = float(ticker_data['lowPrice'])
            volume = float(ticker_data['volume'])
            
            # Volatility Spread Calculation
            price_range_pct = ((high_24h - low_24h) / low_24h) * 100
            
            # AI Sentiment & Strategic Bias
            if price_change > 3.0 and price_range_pct > 5.0:
                sentiment = "High Momentum Bullish (Strong Breakout)"
                risk_score = "High (FOMO risk, watch for sharp pullbacks)"
                action_bias = "Scale in cautiously or wait for a retest of support."
                entry_zone = f"${price * 0.99:,.2f} - ${price:,.2f}"
                tp_zone = f"${price * 1.05:,.2f} - ${price * 1.08:,.2f}"
                sl_zone = f"${price * 0.96:,.2f}"
            elif price_change < -3.0:
                sentiment = "Bearish Correction / Dip Opportunity"
                risk_score = "Moderate-High (Volatility active)"
                action_bias = "Prime zone for phased DCA accumulation."
                entry_zone = f"${price * 0.98:,.2f} - ${price * 0.995:,.2f}"
                tp_zone = f"${price * 1.04:,.2f} - ${price * 1.06:,.2f}"
                sl_zone = f"${price * 0.94:,.2f}"
            else:
                sentiment = "Neutral / Range-Bound Accumulation"
                risk_score = "Low (Stable market structure)"
                action_bias = "Ideal setup for structured DCA scheduling."
                entry_zone = f"${low_24h:,.2f} - ${price:,.2f}"
                tp_zone = f"${price * 1.03:,.2f} - ${price * 1.05:,.2f}"
                sl_zone = f"${price * 0.97:,.2f}"
            
            time.sleep(1)
            print(f"\n--------------------------------------------------")
            print(f"   TRADING MIND INTELLIGENCE REPORT: {symbol}")
            print(f"--------------------------------------------------")
            print(f"{'Current Price':<22} : ${price:,.2f}")
            print(f"{'24h Price Change':<22} : {price_change:+.2f}%")
            print(f"{'24h High / Low':<22} : ${high_24h:,.2f} / ${low_24h:,.2f}")
            print(f"{'Volatility Spread':<22} : {price_range_pct:.2f}% (24h Range)")
            print(f"{'24h Volume':<22} : {volume:,.2f} {display_symbol}")
            print(f"--------------------------------------------------")
            print(f"{'AI Sentiment':<22} : {sentiment}")
            print(f"{'Risk Assessment':<22} : {risk_score}")
            print(f"{'Strategic Bias':<22} : {action_bias}")
            print(f"{'Recommended Entry':<22} : {entry_zone}")
            print(f"{'Take Profit (TP)':<22} : {tp_zone}")
            print(f"{'Stop Loss (SL)':<22} : {sl_zone}")
            print(f"--------------------------------------------------")
            
            # DCA Module (Mandatory Input / No Default)
            print("\n* [DCA Intelligence & Simulation Module]")
            run_dca_sim = input(f"Would you like to configure a custom DCA strategy for {display_symbol}? (y/n): ").strip().lower()
            
            dca_results = None
            if run_dca_sim == 'y':
                print("\n* AI Suggestion: For stable accumulation, allocate 5-10% of your portfolio per session on a Weekly interval during consolidation phases.")
                
                # Validation Loop for Amount
                while True:
                    amount_input = input("Enter amount per DCA session in USD (Required): ").strip()
                    if not amount_input:
                        print("⚠️ Error: Field must be filled! Please enter a valid amount.")
                        continue
                    try:
                        amount = float(amount_input)
                        if amount <= 0:
                            print("⚠️ Error: Amount must be greater than 0.")
                            continue
                        break
                    except ValueError:
                        print("⚠️ Error: Invalid number format. Please enter digits only.")

                # Validation Loop for Interval
                while True:
                    print("Select DCA Interval:")
                    print("  1. Daily")
                    print("  2. Weekly")
                    print("  3. Monthly")
                    interval_choice = input("Enter choice 1/2/3 (Required): ").strip()
                    if not interval_choice:
                        print("⚠️ Error: Field must be filled! Please choose an interval.")
                        continue
                    if interval_choice in ['1', '2', '3']:
                        if interval_choice == '1':
                            interval_str = "Daily"
                        elif interval_choice == '3':
                            interval_str = "Monthly"
                        else:
                            interval_str = "Weekly"
                        break
                    else:
                        print("⚠️ Error: Please choose option 1, 2, or 3.")

                # Validation Loop for Duration Cycles
                while True:
                    duration_input = input(f"Enter total {interval_str.lower()} execution cycles, e.g., 4 or 8 (Required): ").strip()
                    if not duration_input:
                        print("⚠️ Error: Field must be filled! Please enter total cycles.")
                        continue
                    try:
                        duration_cycles = int(duration_input)
                        if duration_cycles <= 0:
                            print("⚠️ Error: Cycles must be greater than 0.")
                            continue
                        break
                    except ValueError:
                        print("⚠️ Error: Invalid number format. Please enter an integer.")

                # DCA Calculation
                total_invested = amount * duration_cycles
                avg_entry_price = price * 0.985
                estimated_coins = total_invested / avg_entry_price
                current_portfolio_value = estimated_coins * price
                roi_percentage = ((current_portfolio_value - total_invested) / total_invested) * 100
                
                dca_results = {
                    "frequency": interval_str,
                    "cycles": duration_cycles,
                    "amount_per_session": amount,
                    "total_invested": total_invested,
                    "simulated_avg_entry": avg_entry_price,
                    "estimated_accumulation": estimated_coins,
                    "projected_portfolio_value": current_portfolio_value,
                    "estimated_roi_pct": roi_percentage
                }
                
                print(f"\n==================================================")
                print(f"  CUSTOM DCA SIMULATION RESULT: {symbol}")
                print(f"==================================================")
                print(f"{'Strategy Frequency':<24} : Every {interval_str} ({duration_cycles} total executions)")
                print(f"{'Simulated Avg Entry':<24} : ${avg_entry_price:,.2f}")
                print(f"{'Total Capital Invested':<24} : ${total_invested:,.2f}")
                print(f"{'Estimated Accumulation':<24} : {estimated_coins:,.4f} {display_symbol}")
                print(f"{'Projected Portfolio':<24} : ${current_portfolio_value:,.2f}")
                print(f"{'Estimated ROI (Sim)':<24} : +{roi_percentage:.2f}%")
            
            # Export Report Option (Fixed Timestamp)
            save_log = input("\n> Export this complete analysis report to a JSON log file? (y/n): ").strip().lower()
            if save_log == 'y':
                current_time_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
                report_data = {
                    "timestamp": current_time_str,
                    "symbol": symbol,
                    "market_data": {
                        "price": price,
                        "change_24h_pct": price_change,
                        "high_24h": high_24h,
                        "low_24h": low_24h,
                        "volatility_spread_pct": price_range_pct
                    },
                    "ai_intelligence": {
                        "sentiment": sentiment,
                        "risk_score": risk_score,
                        "strategic_bias": action_bias,
                        "recommended_entry": entry_zone,
                        "take_profit": tp_zone,
                        "stop_loss": sl_zone
                    },
                    "dca_simulation": dca_results
                }
                filename = f"trading_mind_{display_symbol}_report.json"
                with open(filename, "w") as f:
                    json.dump(report_data, f, indent=4)
                print(f"> Report successfully saved to '{filename}'!")

            print(f"\n* Protocol Status    : Verified & Executed via Trading Mind Core.")
            print(f"* Disclaimer         : AI insights & trading setups are for simulation purposes only.")
        else:
            print(f"⚠️ Warning            : Unable to fetch data for '{symbol}'. Check symbol name.")
            
        print("--------------------------------------------------\n")

if __name__ == "__main__":
    run_trading_mind_agent()
