import requests
from get_token import getToken
from utils import get_url_info
from utils import get_jsonstring_info


def addBuyEntrustmentLimited(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', price=None, volume=None):
    """
    函数功能：委托下单---限价买入
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_buy_entrustment_limited_jsonString %(repr(symbol), repr(market), price, volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json()['msg'] == '操作完成':
        print('下限价买入委托单成功！')
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addSellEntrustmentLimited(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', price=None, volume=None):
    """
    函数功能：委托下单---限价卖出
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_sell_entrustment_limited_jsonString %(repr(symbol), repr(market), price, volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json()['msg'] == '操作完成':
        print('下限价卖出委托单成功！')
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addBuyEntrustmentMarket(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', price=None, market_amount=None):
    """
    函数功能：委托下单---市价买入symbol
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_buy_entrustment_market_jsonString %(repr(symbol), repr(market), market_amount)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json()['msg'] == '操作完成':
        print('市价买入发布成功')
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addSellEntrustmentMarket(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', symbol_volume=None):
    """
    函数功能：委托下单---市价卖出symbol
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_sell_entrustment_market_jsonString %(repr(symbol), repr(market), symbol_volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json()['msg'] == '操作完成':
        print('市价卖出发布成功')
        return r.json()['data']
    else:
        print(r.json()['msg'])

if __name__ == "__main__":
    #addBuyEntrustmentLimited(price=1, volume=1000)
    #addSellEntrustmentLimited(price=1000, volume=100)
    import threading
    """
    for i in range():
        addBuyEntrustmentMarket(market_amount=100)
    for i in range(8):
        addSellEntrustmentMarket(symbol_volume=10)
    """
    print('常规版下单开始......')
    for i in range(100):
        for price in [1.2222, 1.3333, 1.4444, 1.5555, 1.6666]:
            addSellEntrustmentLimited(symbol='MGXT', market='ETH', price=price, volume=10.888888)
        for price in [1.2222, 1.3333, 1.4444, 1.5555, 1.6666]:
            addBuyEntrustmentLimited(symbol='MGXT', market='ETH', price=price, volume=10.888888)
    
    """ for i in range(10):
        for price in [100.8888, 100.9999, 200.8888, 103.7777, 150.8698]:
            addSellEntrustmentLimited(symbol='ETH', market='BTC', price=price, volume=1.88888888)

        for price in [50.8888, 50.9999, 50.8887, 53.7777, 50.8698]:
            addBuyEntrustmentLimited(symbol='ETH', market='BTC', price=price, volume=1.88888888) """
