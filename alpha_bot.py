# ============================================
# GOMEZ ALPHA BOT
# Version 1.0
# ============================================

BOT_NAME = "Gomez Alpha Bot"
MARKET = "EUR/USD"

PRIMARY_TIMEFRAME = "M15"
TREND_TIMEFRAME = "H1"

MODE = "Analysis Only"


def start_bot():
    print("===================================")
    print(BOT_NAME)
    print("===================================")
    print("Market:", MARKET)
    print("Primary Timeframe:", PRIMARY_TIMEFRAME)
    print("Trend Timeframe:", TREND_TIMEFRAME)
    print("Mode:", MODE)
    print("===================================")
    print("Bot started successfully.")


if __name__ == "__main__":
    start_bot()
