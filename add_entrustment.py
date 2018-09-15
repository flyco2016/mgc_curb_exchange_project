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
    jsonString = get_jsonstring_info.add_buy_entrustment_limited_jsonString %(repr(symbol), repr(market), price, volume, price*volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json() == '操作完成':
        print('下限价买入委托单成功！')
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addSellEntrustmentLimited(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', price=None, volume=None):
    """
    函数功能：委托下单---限价买入
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_sell_entrustment_limited_jsonString %(repr(symbol), repr(market), price, volume, price*volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json() == '操作完成':
        print('下限价卖出委托单成功！')
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addBuyEntrustmentMarket(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', price=None, volume=None):
    """
    函数功能：委托下单---限价买入
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_buy_entrustment_limited_jsonString %(repr(symbol), repr(market), price, volume, price*volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json() == '操作完成':
        print('下限价买入委托单成功！')
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addSellEntrustmentMarket(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ', price=None, volume=None):
    """
    函数功能：委托下单---限价买入
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_sell_entrustment_limited_jsonString %(repr(symbol), repr(market), price, volume, price*volume)
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_entrustment_url, data=data, headers=headers)
    if r.json() == '操作完成':
        print('下限价卖出委托单成功！')
        return r.json()['data']
    else:
        print(r.json()['msg'])

if __name__ == "__main__":
    #addBuyEntrustmentLimited(price=1, volume=1000)
    addSellEntrustmentLimited(price=1000, volume=100)
    
    