import re
from telethon import TelegramClient, events
from alpaca_trade_api import REST

# Telegram API Daten
api_id = 32300826
api_hash = "24545744578321d45950ee2dcddaa598"
client = TelegramClient("session_name", api_id, api_hash)

# Alpaca API Daten (Paper Trading empfohlen!)
ALPACA_API_KEY = "PKO2NOOTI2DUCCTSTIN6PQFHJH"
ALPACA_SECRET_KEY = "7ziVQxNabAxzR1qbi4hqRwszb5mkBCxBg2YpWHrM4hyy"
BASE_URL = "https://paper-api.alpaca.markets"

alpaca = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, BASE_URL)

# Handler für neue Telegram-Signale
@client.on(events.NewMessage(chats="NationForex"))
async def handler(event):
    signal = event.message.text.strip()
    print("Neues Signal:", signal)

    # Regex zum Parsen: Richtung, Symbol, Menge, SL, TP
    match = re.match(r"(BUY|SELL)\s+(\w+)\s+(\d+)\s+SL=(\d+\.?\d*)\s+TP=(\d+\.?\d*)", signal)
    if match:
        side, symbol, qty, sl, tp = match.groups()
        qty = int(qty)
        sl = float(sl)
        tp = float(tp)

        # Market Order
        order = alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side=side.lower(),   # "buy" oder "sell"
            type="market",
            time_in_force="gtc"
        )
        print("Market Order ausgeführt:", order)

        # Stop-Loss Order
        alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side="sell" if side == "buy" else "buy",
            type="stop",
            stop_price=sl,
            time_in_force="gtc"
        )
        print("Stop-Loss gesetzt bei:", sl)

        # Take-Profit Order
        alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side="sell" if side == "buy" else "buy",
            type="limit",
            limit_price=tp,
            time_in_force="gtc"
        )
        print("Take-Profit gesetzt bei:", tp)

client.start()
print("Bot läuft – wartet auf neue Signale...")
client.run_until_disconnected()
