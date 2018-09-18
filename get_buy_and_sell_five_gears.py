import requests
import json
from utils import get_url_info


def getBuyFiveGears(symbol='BTC', market='NZ'):
    """
    函数功能：获取买五档数据
    """
    payload = {"tradeCode":"{market}:{symbol}".format(market=market, symbol=symbol), 'size': 5}
    r = requests.post(get_url_info.get_buy_and_sell_five_gears_url, data=json.dumps(payload))
    if 'buy' in r.json().keys():
        return (r.json()['buy'])
    else:
        print('买五档为空')

def getSellFiveGears(symbol='BTC', market='NZ'):
    """
    函数功能：获取卖五档数据
    """
    payload = {"tradeCode":"{market}:{symbol}".format(market=market, symbol=symbol), 'size': 5}
    r = requests.post(get_url_info.get_buy_and_sell_five_gears_url, data=json.dumps(payload))
    if 'sell' in r.json().keys():
        return (r.json()['sell'])
    else:
        print('卖五档为空')

if __name__ == "__main__":
    import time
    import random
    import add_entrustment
    
    start= time.time()
    for i in range(100):
        # 发布委托单
        for price in [100.8888, 100.9999, 200.8888, 103.7777, 150.8698]:
            add_entrustment.addSellEntrustmentLimited(price=price, volume=1.88888888)

        for price in [51.8888, 52.9999, 53.8888, 54.7777, 55.8698]:
            add_entrustment.addBuyEntrustmentLimited(price=price, volume=100.88888888)
        

        """
        rlist = []
        for each_item in (getSellFiveGears(), getBuyFiveGears()): 
            for i in each_item:
                for j in sorted([[(k, v)] for k, v in i.items()], key=lambda x: x[0][1], reverse=True):
                    print(j)
                    #print('价格', ":", j[0][1], '==>', '总量' , ":", j[1][1])
                print('\n')
        

        #for j in sorted([[(k, v)] for k, v in i.items()], key=lambda x: x[0][1], reverse=True)
        """
        """
        rlist_0 = [each_item for each_item in getBuyFiveGears()]
        rlist_1 = [list(i.items()) for i in rlist_0]
        rlist_2 = sorted(rlist_1, key=lambda x: x[0][1], reverse=True)
        print(rlist_0)
        print(rlist_1)
        print(rlist_2)
        #print(getSellFiveGears())
        """
        # 获取买卖五档
        for gear in (getBuyFiveGears(), getSellFiveGears()):
            for j in sorted([list(i.items()) for i in [each_item for each_item in gear]], key=lambda x: x[0][1], reverse=True):
                print('价格', ":", j[0][1], '<==>', '总量' , ":", j[1][1], '<==>', "总额", ':', float(j[0][1])*float(j[1][1]))
    print(time.time()-start)
    
    
