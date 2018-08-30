import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import init_fund_account_in_db
import advertising
import del_ads_in_db

currency_tuple = ('BYC', 'BTC', 'ETH', 'KBC', 'NZ', 'USDT')
#payment_dict = {"bankcard": 1, "Alipay": 2, "WeChatPay": 4}

def getBuyAd(user_name='17727820013', password='123456', currency=None):
    """
    获取商家发布的广告求购单列表
    """
    try:
        ad_order_list = []
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        headers = {"token": str(mytoken)}
        for each_page in range(1, 10):
            jsonString = get_jsonstring_info.get_buy_ad_list_jsonString %(repr(currency), each_page)        
            data = dict(jsonString=jsonString)
            r = requests.post(get_url_info.get_ad_list_url, data=data, headers=headers)
            ad_order_list.extend(r.json()['data']['list'])
        return [x['advertisingOrderId'] for x in ad_order_list]
    except Exception as err:
        print(err)

def getSellAd(user_name='17727820013', password='123456', currency=None):
    """
    获取商家发布的广告卖单列表
    """
    try:
        ad_order_list = []
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        headers = {"token": str(mytoken)}
        for each_page in range(1, 10):
            jsonString = get_jsonstring_info.get_sell_ad_list_jsonString %(repr(currency), each_page)        
            data = dict(jsonString=jsonString)
            r = requests.post(get_url_info.get_ad_list_url, data=data, headers=headers)
            ad_order_list.extend(r.json()['data']['list'])
        return [x['advertisingOrderId'] for x in ad_order_list]
    except Exception as err:
        print(err)


if __name__ == "__main__":
    """
    print("......初始化法币资金账户的NZ......")
    init_fund_account_in_db.initUserFundAccount(fund_type='UserCoin2CoinFunds', 
    user_name='手机商家', currency='NZ', available_balance=10000, frozen_balance=0)
    
    print('......发布11条1CNY的广告......')
    for i in range(11):
        advertising.limitedPriceBuyAd(user_name="17727820013", currency="NZ", price=1, amount=1000,
        floor=100, ceiling=1000)
    """
    print('......获取这些广告id......')
    #r = getMerchantBuyAd(user_name='17727820013', password='123456', currency='NZ')
    #print(r)
    """
    for i in [x["advertisingOrderId"] for x in r if (x['type'] == 2)]:
        print(i)
    """
    advertising.limitedPriceBuyAd(currency='BTC', price=1, amount=1000, floor=1, ceiling=1000)
    advertising.marketPriceSellAd(currency='BTC', amount=1000, floor=1, ceiling=1000)

    r1 = getBuyAd(user_name='17727820013', password='123456', currency='BTC')
    print(r1)

    r2 = getSellAd(currency='BTC')
    print(r2)
    
