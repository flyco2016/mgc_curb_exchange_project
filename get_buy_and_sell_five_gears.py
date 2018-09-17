import requests
import json
from utils import get_url_info


def getBuyFiveGears(symbol='BTC', market='NZ'):
    """
    函数功能：获取买五档数据
    """
    payload = {"data": [{"tradeCode":"{market}:{symbol}".format(market=market, symbol=symbol), 'size': 5}]}
    r = requests.post(get_url_info.get_buy_and_sell_five_gears_url, data=json.dumps(payload))
    print(r.json())

def getSellFiveGears(symbol='BTC', market='NZ'):
    """
    函数功能：获取买五档数据
    """
    payload = {"data": [{"tradeCode":"{market}:{symbol}".format(market=market, symbol=symbol), 'size': 5}]}
    r = requests.post(get_url_info.get_buy_and_sell_five_gears_url, data=json.dumps(payload))
    print(r.json())

if __name__ == "__main__":
    getBuyFiveGears()
    getSellFiveGears()
