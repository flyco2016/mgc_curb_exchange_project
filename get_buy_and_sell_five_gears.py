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
    import threading

    start= time.time()
    sell_list = [15.0881, 15.0882, 15.0883, 15.0884, 15.0885]
    buy_list = [10.0881, 10.0882, 10.0883, 10.0884, 10.0885]
    
    print('常规版下单开始......')
    for i in range(100):
        # 发布委托单
        #sell_list = [29644.2850, 29051.4863, 29009.6223, 28648.1687, 28605.5354]
        #buy_list = [27917.8994, 27762.6868, 27574.7470, 27189.3450, 27095.9253]
        for price in sell_list:
            add_entrustment.addSellEntrustmentLimited(symbol='BTC', market='NZ', price=price, volume=1.8888888)
            time.sleep(0.5)

        for price in buy_list:
            add_entrustment.addBuyEntrustmentLimited(symbol='BTC', market='NZ', price=price, volume=1.8888888)
            time.sleep(0.5)
    
    
    print('伪多线程版下单开始......')
    for i in range(50):
        
        for price in sell_list:
            sell_thread = threading.Thread(target=add_entrustment.addSellEntrustmentLimited, kwargs={"symbol":'BTC', "market":'NZ', "price":price, "volume":1.888888})
            sell_thread.setDaemon(True)
            sell_thread.start()
        sell_thread.join()

        for price in buy_list:
            buy_thread = threading.Thread(target=add_entrustment.addBuyEntrustmentLimited, kwargs={"symbol":'BTC', "market":'NZ', "price":price, "volume":1.888888})
            buy_thread.setDaemon(True)
            buy_thread.start()    
        buy_thread.join()

    """
    rlist = []
    for each_item in (getSellFiveGears(), getBuyFiveGears()): 
        for i in each_item:
            for j in sorted([[(k, v)] for k, v in i.items()], key=lambda x: x[0][1], reverse=True):
                print(j)
                #print('价格', ":", j[0][1], '==>', '总量' , ":", j[1][1])
            print('\n')
        

    #for j in sorted([[(k, v)] for k, v in i.items()], key=lambda x: x[0][1], reverse=True)
    
    rlist_0 = [each_item for each_item in getBuyFiveGears()]
    rlist_1 = [list(i.items()) for i in rlist_0]
    rlist_2 = sorted(rlist_1, key=lambda x: x[0][1], reverse=True)
    print(rlist_0)
    print(rlist_1)
    print(rlist_2)
    #print(getSellFiveGears())
    """

        # 获取买卖五档
        #frozen_NZ = 0
    
    for gear in (getBuyFiveGears(symbol='BTC', market='NZ'), getSellFiveGears(symbol='BTC', market='NZ')):
        for j in sorted([list(i.items()) for i in [each_item for each_item in gear]], key=lambda x: x[0][1], reverse=True):
            #frozen_NZ += float(j[0][1])*float(j[1][1])
            print('价格', ":", j[0][1], '<==>', '总量' , ":", j[1][1], '<==>', "总额", ':', float(j[0][1])*float(j[1][1]))
    print(time.time()-start)
    #print('BTC冻结金额:', 0.88888888*50*5*2)
    #print('NZ冻结金额:', frozen_NZ)
    #print('NZ冻结金额:', sum(filter(lambda x:x*200, buy_list)))

    


    
    
