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
