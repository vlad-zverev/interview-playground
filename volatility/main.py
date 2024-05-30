"""
https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#klinecandlestick-data
https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=60

calcualte volatility for last 1 hour for 5 symbols:
BTCUSDT
ETHBTC
LTCBTC
DGBBTC
DOGEBTC

formula:
volatility = (max_high - min_low) / min_low * 100

"""
