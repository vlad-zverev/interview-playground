"""
Calculate volatility for last 1 hour for few symbols:

BTCUSDT
ETHBTC
LTCBTC
ABOBABTC
DGBBTC
DOGEBTC

Formula:
volatility = (max_high - min_low) / min_low * 100

Data source:
https://api.binance.com/api/v3/klines
Docs for method:
https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#klinecandlestick-data

Use OOP approach
Imagine that in the future you have to implement few other data sources
Load data concurrently with async
Code should be production ready, well optimized, typed, with PEP8 respect
"""
