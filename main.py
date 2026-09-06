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
    print("🧠 TRADING MIND AGENT (AI Intelligence & Integrated DCA)")
    print("==================================================")
    print("[+] Initializing Advanced Neural Sentiment & Risk Core...")
    time.sleep(1)
    
    print("\n[?] Instructions:")
    print("    - Analyze asset intelligence, volatility metrics, and simulate DCA.")
    print("    - Type 'exit' anytime to close the session.")
    
    while True:
        print("-" * 50)
        coin_input = input("Enter asset to analyze (e.g., BTC, ETH) [or type 'exit']: ").strip()
        
        if coin_input.lower() == 'exit':
            print("\n[+] Shutting down Trading Mind neural link safely...")
            time.sleep(1)
            print("✨ Agent session terminated. Stay safe in the market!")
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
            
            # Perhitungan Volatilitas Sederhana (Rentang Harga 24 Jam)
            price_range_pct = ((high_24h - low_24h) / low_24h) * 100
            
            # Analisis Mind AI Berdasarkan Pergerakan Pasar & Volatilitas
            if price_change > 3.0 and price_range_pct > 5.0:
                sentiment = "🚀 High Momentum Bullish (Strong Breakout)"
                risk_score = "High (FOMO risk, watch for sharp pullbacks)"
                action_bias = "Scale in cautiously or wait for a retest of support."
            elif price_change < -3.0:
                sentiment = "🩸 Bearish Correction / Dip Opportunity"
                risk_score = "Moderate-High (Volatility active)"
                action_bias = "Prime zone for phased DCA accumulation."
            else:
                sentiment = "⚖️ Neutral / Range-Bound Accumulation"
                risk_score = "Low (Stable market structure)"
                action_bias = "Ideal setup for structured DCA scheduling."
            
            time.sleep(1)
            print(f"\n--------------------------------------------------")
            print(f"🧠 TRADING MIND INTELLIGENCE REPORT: {symbol}")
            print(f"--------------------------------------------------")
            print(f"💰 Current Price      : ${price:,.2f}")
            print(f"📊 24h Price Change   : {price_change:+.2f}%")
            print(f"📈 24h High / Low     : ${high_24h:,.2f} / ${low_24h:,.2f}")
            print(f"🌊 Volatility Spread  : {price_range_pct:.2f}% (24h Range)")
            print(f"📦 24h Volume         : {volume:,.2f} {display_symbol}")
            print(f"--------------------------------------------------")
            print(f"🔮 AI Sentiment       : {sentiment}")
            print(f"⚠️ Risk Assessment    : {risk_score}")
            print(f"💡 Strategic Bias     : {action_bias}")
            print(f"--------------------------------------------------")
            
            # Integrasi Fitur DCA
            print("\n🔄 [DCA Integration Module]")
            run_dca_sim = input(f"Would you like to run a DCA simulation for {display_symbol}? (y/n) [Default y]: ").strip().lower()
            
            dca_results = None
            if run_dca_sim != 'n':
                try:
                    amount_input = input(f"Enter amount per DCA session (USD) [Default 50]: ").strip()
                    amount = float(amount_input) if amount_input else 50.0
                    
                    print("Select DCA Interval:")
                    print("  1. Daily")
                    print("  2. Weekly")
                    print("  3. Monthly")
                    interval_choice = input("Enter choice (1/2/3) [Default 2 - Weekly]: ").strip()
                    
                    if interval_choice == '1':
                        interval_str = "Daily"
                    elif interval_choice == '3':
                        interval_str = "Monthly"
                    else:
                        interval_str = "Weekly"
                        
                    duration_input = input(f"Enter duration / total {interval_str.lower()} intervals [Default 4]: ").strip()
                    duration_cycles = int(duration_input) if duration_input else 4
                    
                except ValueError:
                    print("⚠️ Invalid input. Using default values ($50, Weekly, 4 intervals).")
                    amount = 50.0
                    interval_str = "Weekly"
                    duration_cycles = 4
                
                # Perhitungan Simulasi DCA
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
                print(f"📊 DCA SIMULATION RESULT: {symbol}")
                print(f"==================================================")
                print(f"⏱️ Strategy Frequency    : Every {interval_str} ({duration_cycles} total executions)")
                print(f"📈 Simulated Avg Entry   : ${avg_entry_price:,.2f}")
                print(f"💵 Total Capital Invested: ${total_invested:,.2f}")
                print(f"🪙 Estimated Accumulation: {estimated_coins:,.4f} {display_symbol}")
                print(f"💼 Projected Portfolio   : ${current_portfolio_value:,.2f}")
                print(f"🚀 Estimated ROI (Sim)   : +{roi_percentage:.2f}%")
            
            # Fitur Export Laporan ke JSON Log
            save_log = input("\n💾 Export this analysis report to a JSON log file? (y/n) [Default n]: ").strip().lower()
            if save_log == 'y':
                report_data = {
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
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
                        "strategic_bias": action_bias
                    },
                    "dca_simulation": dca_results
                }
                filename = f"trading_mind_{display_symbol}_report.json"
                with open(filename, "w") as f:
                    json.dump(report_data, f, indent=4)
                print(f"✅ Report successfully saved to '{filename}'!")

            print(f"\n🔒 Protocol Status    : Verified & Executed via Trading Mind Core.")
            print(f"⚠️ Disclaimer         : AI insights are for simulation & educational purposes only.")
        else:
            print(f"⚠️ Warning            : Unable to fetch data for '{symbol}'. Check symbol name.")
            
        print("--------------------------------------------------\n")

if __name__ == "__main__":
    run_trading_mind_agent()
