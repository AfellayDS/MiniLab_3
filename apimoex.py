import requests
import datetime
import pandas


def convert(json):
    """Service function. Convert data from JSON format to Pandas DataFrame."""
    table = []
    for row in json['data']:
        dct = dict()
        for i, label in enumerate(json['columns']):
            if json['metadata'][label]['type'] == 'datetime':
                row[i] = datetime.datetime.strptime(row[i], '%Y-%m-%d %H:%M:%S')
            if json['metadata'][label]['type'] == 'date':
                row[i] = datetime.datetime.strptime(row[i], '%Y-%m-%d')
            dct[label] = row[i]
        table.append(dct)
    table = pandas.DataFrame(table)
    return table


def get_specification(security):
    """Get tool specification."""
    url = f'https://iss.moex.com/iss/securities/{security}.json?lang=en'
    data = requests.get(url).json()
    data = convert(data['description'])
    return data


def get_dividends(security):
    """Get the company's dividend history."""
    url = f'https://iss.moex.com/iss/securities/{security}/dividends.json'
    data = requests.get(url).json()
    data = convert(data['dividends'])
    return data


def get_market_candles_block(security, start, first_date, last_date, interval):
    """Service function. Receive data for a request and return all information in one cycle."""
    url = f'https://iss.moex.com/iss/engines/stock/markets/shares/securities/{security}/candles.json?'
    parameters = f'start={start}&from={first_date}&till={last_date}&interval={interval}'
    j_block = requests.get(url + parameters).json()
    return j_block['candles']


def get_market_candles(security, first_date, last_date, interval):
    """
    Get candles of the specified instrument on the market
    for the main trading mode for the date interval.

    :param security: security ticker
    :param first_date: first date of quote history
    :param last_date: last date of quote history
    :param interval: candle size
    :return: dictionary containing the necessary information
    """
    start = 0
    data = get_market_candles_block(security, start, first_date, last_date, interval)
    delta = len(data['data'])
    while delta > 0:
        start += delta
        block = get_market_candles_block(security, start, first_date, last_date, interval)
        data['data'] += block['data']
        delta = len(block['data'])
    data = convert(data)
    return data
