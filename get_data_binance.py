import config
import csv
from binance.client import Client

client = Client(config.API_KEY, config.SECRET_KEY)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)


csvfile = open('btc15m.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=' ')
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()
