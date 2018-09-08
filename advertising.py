import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import get_international_quotation


#currency_tuple = ('BYC', 'BTC', 'ETH', 'KBC', 'NZ', 'USDT')
#payment_dict = {"bankcard": 1, "Alipay": 2, "WeChatPay": 4}

def limitedPriceBuyAd(user_name='17727820013', password='123456', currency=None, 
payment=7, price=None, amount=None, floor=None, ceiling=None):
    """
    发布限价买入广告
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.limited_price_buy_ad_jsonString %(repr(currency), payment, price, 
        amount, floor, ceiling)        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.advertising_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print("发布限价买入广告成功！")
        if r.json()['msg'] == '每个账户只能挂一张买单':
            print("该用户已经发布了一个买单，想要发布，请升级账户或者撤单再发布")
    except Exception as err:
        print(err)

def marketPriceBuyAd(user_name='17727820013', password='123456', currency=None, 
payment=7, amount=None, floor=None, ceiling=None):
    """
    发布市价买入广告
    """
    try:
        quotation = get_international_quotation.getInternationalQuotation(currency)
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.market_price_buy_ad_jsonString %(repr(currency), payment, 
        amount, floor/quotation, ceiling/quotation)        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.advertising_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print("发布市价买入广告成功！")
        if r.json()['msg'] == '每个账户只能挂一张买单':
            print("该用户已经发布了一个买单，想要发布，请升级账户或者撤单再发布")
    except Exception as err:
        print(err)

def limitedPriceSellAd(user_name='17727820013', password='123456', currency=None, 
payment=7, price=None, amount=None, floor=None, ceiling=None):
    """
    发布限价卖出广告
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.limited_price_sell_ad_jsonString %(repr(currency), payment, price, 
        amount, floor, ceiling)        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.advertising_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print("发布限价卖出广告成功！")
        elif r.json()['msg'] == '每个账户只能挂一张卖单':
            print("该用户已经发布了一个卖单，想要发布，请升级账户或者撤单再发布")
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)
    
def marketPriceSellAd(user_name='17727820013', password='123456', currency=None, 
payment=7, amount=None, floor=None, ceiling=None):
    """
    发布市价卖出广告
    """
    try:
        quotation = get_international_quotation.getInternationalQuotation(currency)
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.market_price_sell_ad_jsonString %(repr(currency), payment, 
        amount, floor/quotation, ceiling/quotation)        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.advertising_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print("发布市价卖出广告成功！")
        elif r.json()['msg'] == '每个账户只能挂一张卖单':
            print("该用户已经发布了一个卖单，想要发布，请升级账户或者撤单再发布")
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)



if __name__ == "__main__":
   
    # 发布十个限价买入广告
    for i in range(10):
        limitedPriceBuyAd(user_name="17727820013", currency="NZ", price=1, amount=1000,
        floor=100, ceiling=1000)
    
    
    # 发布十个市价买入广告
    for i in range(10):
        marketPriceBuyAd(user_name="17727820013", currency="NZ", amount=1000,
        floor=100, ceiling=1000)
    

    # 发布十个限价卖出广告
    for i in range(10):
        limitedPriceSellAd(user_name="17727820013", currency="NZ", price=1, amount=1000,
        floor=100, ceiling=1000)
    
    # 发布十个市价卖出广告
    for i in range(10):
        marketPriceSellAd(user_name="17727820013", currency="NZ", amount=1000,
        floor=100, ceiling=1000)