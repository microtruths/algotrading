from alpha_vantage.cryptocurrencies import CryptoCurrencies
from pprint import pprint
import json
import argparse


def save_dataset(symbol, market, time_window):
    credentials = json.load(open('creds.json', 'r'))
    api_key = credentials['av_api_key']
    print(symbol, time_window)
    cc = CryptoCurrencies(key=api_key, output_format='pandas')
    if time_window == 'daily':
        data, meta_data = cc.get_digital_currency_daily(symbol, market)
    elif time_window == 'weekly':
        data, meta_data = cc.get_digital_currency_weekly(symbol, market)
    elif time_window == 'monthly':
        data, meta_data = cc.get_digital_currency_monthly(symbol, market)

    pprint(data.head(10))

    data.to_csv(f'./{symbol}_{market}_{time_window}.csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
    parser.add_argument('market', type=str, choices=[
                        'USD', 'CNY', 'BTC'], help="the time period you want to download the stock history for")
    parser.add_argument('time_window', type=str, choices=[
                        'daily', 'weekly', 'monthly'], help="the time period you want to download the stock history for")

    namespace = parser.parse_args()
    save_dataset(**vars(namespace))
