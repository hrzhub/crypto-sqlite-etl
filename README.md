🪙 Crypto Market ETL Project

A lightweight ETL (Extract, Transform, Load) pipeline that pulls live cryptocurrency data from the CoinGecko public API. It cleans and transforms the data using Pandas, and stores it in a SQLite database.

🚀 Overview

This project demonstrates a fundamental data engineering workflow:

- Extract → Pulls real-time market data for the top 50 cryptocurrencies.
- Transform → Selects and cleans key columns like id, symbol, price, and market_cap.
- Load → Saves the results into a local SQLite database (crypto_data.db).
- Analyze → Runs SQL queries to display:
  🏆 Top 5 coins by market capitalization
  📈 Top 3 coins to watch today (based on 24-hour performance)

🧠 Tech Stack

- Language: Python 3
- Libraries: requests, pandas, sqlite3, datetime
- Database: SQLite
- API Source: CoinGecko Public API

⚙️ How It Works

- Fetch data from CoinGecko’s /markets endpoint.
- Convert JSON response into a Pandas DataFrame.
- Add a UTC timestamp for data freshness tracking.
- Load the DataFrame into a SQLite table crypto_prices.
- Query and display top-performing cryptocurrencies directly via SQL.

💾 Clone & Run

1. Clone this repository

   > git clone https://github.com/muhammad9harraz/crypto_sqlite.git
   > cd crypto_sqlite

2. Install dependencies

   > pip install pandas requests

3. Run the ETL pipeline

   > python crypto_etl.py

📊 Sample Output

Data loaded into crypto_data.db successfully

-----Table-----
id symbol ... price_change_percentage_24h timestamp
0 bitcoin btc ... -2.14915 2025-10-14 16:17:41.114308+00:00
1 ethereum eth ... -1.50280 2025-10-14 16:17:41.114308+00:00
2 tether usdt ... -0.01873 2025-10-14 16:17:41.114308+00:00
3 binancecoin bnb ... -4.07279 2025-10-14 16:17:41.114308+00:00
4 ripple xrp ... -3.90144 2025-10-14 16:17:41.114308+00:00
5 solana sol ... 2.15258 2025-10-14 16:17:41.114308+00:00
6 usd-coin usdc ... -0.00005 2025-10-14 16:17:41.114308+00:00
7 staked-ether steth ... -1.65145 2025-10-14 16:17:41.114308+00:00
8 dogecoin doge ... -3.59990 2025-10-14 16:17:41.114308+00:00
9 tron trx ... -2.18815 2025-10-14 16:17:41.114308+00:00
10 cardano ada ... -2.96989 2025-10-14 16:17:41.114308+00:00
11 wrapped-steth wsteth ... -1.48489 2025-10-14 16:17:41.114308+00:00
12 wrapped-beacon-eth wbeth ... -1.38772 2025-10-14 16:17:41.114308+00:00
13 wrapped-bitcoin wbtc ... -1.66274 2025-10-14 16:17:41.114308+00:00
14 chainlink link ... -3.99055 2025-10-14 16:17:41.114308+00:00
15 figure-heloc figr_heloc ... 2.51938 2025-10-14 16:17:41.114308+00:00
16 ethena-usde usde ... 0.14517 2025-10-14 16:17:41.114308+00:00
17 wrapped-eeth weeth ... -1.42922 2025-10-14 16:17:41.114308+00:00
18 hyperliquid hype ... -0.71051 2025-10-14 16:17:41.114308+00:00
19 stellar xlm ... -3.50993 2025-10-14 16:17:41.114308+00:00
20 bitcoin-cash bch ... -2.17211 2025-10-14 16:17:41.114308+00:00
21 sui sui ... -1.96570 2025-10-14 16:17:41.114308+00:00
22 avalanche-2 avax ... -0.23775 2025-10-14 16:17:41.114308+00:00
23 weth weth ... -1.43891 2025-10-14 16:17:41.114308+00:00
24 binance-bridged-usdt-bnb-smart-chain bsc-usd ... 0.25755 2025-10-14 16:17:41.114308+00:00
25 leo-token leo ... -0.17459 2025-10-14 16:17:41.114308+00:00
26 usds usds ... 0.02518 2025-10-14 16:17:41.114308+00:00
27 hedera-hashgraph hbar ... -1.65391 2025-10-14 16:17:41.114308+00:00
28 coinbase-wrapped-btc cbbtc ... -2.13658 2025-10-14 16:17:41.114308+00:00
29 usdt0 usdt0 ... -0.11736 2025-10-14 16:17:41.114308+00:00
30 litecoin ltc ... -2.91032 2025-10-14 16:17:41.114308+00:00
31 mantle mnt ... -4.08647 2025-10-14 16:17:41.114308+00:00
32 shiba-inu shib ... -3.15402 2025-10-14 16:17:41.114308+00:00
33 whitebit wbt ... -1.87752 2025-10-14 16:17:41.114308+00:00
34 the-open-network ton ... -0.30456 2025-10-14 16:17:41.114308+00:00
35 ethena-staked-usde susde ... 0.05454 2025-10-14 16:17:41.114308+00:00
36 crypto-com-chain cro ... -3.77796 2025-10-14 16:17:41.114308+00:00
37 monero xmr ... -3.16325 2025-10-14 16:17:41.114308+00:00
38 polkadot dot ... -2.96712 2025-10-14 16:17:41.114308+00:00
39 dai dai ... 0.15531 2025-10-14 16:17:41.114308+00:00
40 bittensor tao ... 12.51212 2025-10-14 16:17:41.114308+00:00
41 zcash zec ... 7.03541 2025-10-14 16:17:41.114308+00:00
42 uniswap uni ... -0.73460 2025-10-14 16:17:41.114308+00:00
43 world-liberty-financial wlfi ... 0.66923 2025-10-14 16:17:41.114308+00:00
44 aave aave ... -1.18003 2025-10-14 16:17:41.114308+00:00
45 okb okb ... -2.48300 2025-10-14 16:17:41.114308+00:00
46 memecore m ... 1.97257 2025-10-14 16:17:41.114308+00:00
47 bitget-token bgb ... -2.07404 2025-10-14 16:17:41.114308+00:00
48 pepe pepe ... -5.02427 2025-10-14 16:17:41.114308+00:00
49 ethena ena ... -0.40774 2025-10-14 16:17:41.114308+00:00

[50 rows x 7 columns]

-----Top 5 Coins-----
Name Symbol Market_Cap
0 Bitcoin btc 2242462864293
1 Ethereum eth 491692796228
2 Tether usdt 180147481251
3 BNB bnb 170473124066
4 XRP xrp 149110496305

-----Top 3 Coins to Watch Today (based on 24h growth)-----
Name Symbol Price_Change_24h
0 Bittensor tao 12.51212
1 Zcash zec 7.03541
2 Figure Heloc figr_heloc 2.51938
