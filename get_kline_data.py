import requests
import json
from utils import get_url_info


def getOneMinKlineData(symbol='BTC', market='NZ'):
    """
    函数功能：获取分辨率为1min的数据
    """
    payload = {"symbol":"{symbol}:{market}".format(market=market, symbol=symbol), 
    "from": 1537159373, "to": 1537171373,'resolution': '1'}

    r = requests.post(get_url_info.get_kline_data_url, data=json.dumps(payload))
    return r.json()['data']

def getFiveMinsKlineData(symbol='BTC', market='NZ'):
    """
    函数功能：获取分辨率为5mins的数据
    """
    payload = {"symbol":"{symbol}:{market}".format(market=market, symbol=symbol), 
    "from": 1537159373, "to": 1537171373,'resolution': '5'}

    r = requests.post(get_url_info.get_kline_data_url, data=json.dumps(payload))
    return r.json()['data']

def getFifteenMinsKlineData(symbol='BTC', market='NZ'):
    """
    函数功能：获取分辨率为15mins的数据
    """
    payload = {"symbol":"{symbol}:{market}".format(market=market, symbol=symbol), 
    "from": 1537159373, "to": 1537171373,'resolution': '15'}

    r = requests.post(get_url_info.get_kline_data_url, data=json.dumps(payload))
    return r.json()['data']

def getThirtyMinsKlineData(symbol='BTC', market='NZ'):
    """
    函数功能：获取分辨率为30mins的数据
    """
    payload = {"symbol":"{symbol}:{market}".format(market=market, symbol=symbol), 
    "from": 1537159373, "to": 1537171373,'resolution': '30'}

    r = requests.post(get_url_info.get_kline_data_url, data=json.dumps(payload))
    return r.json()['data']

def getOneHourKlineData(symbol='BTC', market='NZ'):
    """
    函数功能：获取分辨率为1h的数据
    """
    payload = {"symbol":"{symbol}:{market}".format(market=market, symbol=symbol), 
    "from": 1537159373, "to": 1537171373,'resolution': '60'}

    r = requests.post(get_url_info.get_kline_data_url, data=json.dumps(payload))
    return r.json()['data']

if __name__ == '__main__':
    print((1537171373-1537153373)/60)
    print(len(getOneMinKlineData()))
    print(len(getFiveMinsKlineData()))
    print(len(getFifteenMinsKlineData()))
    print(len(getThirtyMinsKlineData()))
    print(len(getOneHourKlineData()))