import requests
import pandas as pd
import sqlite3
from datetime import datetime, timezone

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 50, "page": 1}
resp = requests.get(url, params=params, timeout=10)
resp.raise_for_status()
data = resp.json()

df = pd.DataFrame(data)[["id", "symbol", "name", "current_price", "market_cap", "price_change_percentage_24h"]]
df["timestamp"] = datetime.now(timezone.utc)

conn = sqlite3.connect("crypto_data.db")
df.to_sql("crypto_prices", conn, if_exists="replace", index=False)

print("Data loaded into crypto_data.db successfully")

print("\n-----Table-----")
print(df)

top5_coins = pd.read_sql_query("""
SELECT name AS Name,
symbol AS Symbol,
market_cap AS Market_Cap
FROM crypto_prices
ORDER BY Market_Cap DESC
LIMIT 5
""", conn)
print("\n-----Top 5 Coins-----")
print(top5_coins)

top_gainers = pd.read_sql_query("""
SELECT name AS Name,
symbol AS Symbol,
price_change_percentage_24h AS Price_Change_24h
FROM crypto_prices
WHERE Price_Change_24h IS NOT NULL
ORDER BY Price_Change_24h DESC
LIMIT 3
""", conn)
print("\n-----Top 3 Coins to Watch Today (based on 24h growth)-----")
print(top_gainers)

conn.close()