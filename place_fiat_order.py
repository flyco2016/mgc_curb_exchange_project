import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import get_ads_info_in_db
import get_international_quotation
import cancel_order


def buyCurrencyByAmount(user_name=None, password='123456', ad_ID_NO=None, trade_amount=None):
    """
    按照总额买入货币
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        advertiser_userid = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['userId']      
        currency = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['tradeCode']
        unit_price = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['priceVal']
        #quotation_now = get_international_quotation.getInternationalQuotation(currency=currency)
        headers = {"token": mytoken}

        if get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 2:
            if get_ads_info_in_db.judgeIfLimitedPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.buy_fiat_order_limited_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_amount, trade_amount/unit_price, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
            elif get_ads_info_in_db.judgeIfMarketdPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.buy_fiat_order_market_by_amount_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_amount, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
        elif get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 1:
            print('该广告单不是卖出广告单')
    except Exception as err:
        print(err)
    
def buyCurrencyByQuantity(user_name=None, password='123456', ad_ID_NO=None, trade_quantity=None):
    """
    按照数量买入货币
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        advertiser_userid = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['userId']       
        currency = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['tradeCode']
        unit_price = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['priceVal']
        quotation_now = get_international_quotation.getInternationalQuotation(currency=currency)
        headers = {"token": mytoken}

        if get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 2:
            if get_ads_info_in_db.judgeIfLimitedPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.buy_fiat_order_limited_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_quantity*unit_price, trade_quantity, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
            elif get_ads_info_in_db.judgeIfMarketdPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.buy_fiat_order_market_by_quantity_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_quantity*quotation_now, trade_quantity, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
        elif get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 1:
            print('该广告单不是卖出广告单')
    except Exception as err:
        print(err)
    
def sellCurrencyByAmount(user_name=None, password='123456', ad_ID_NO=None, trade_amount=None):
    """
    按照总额卖出货币
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        advertiser_userid = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['userId']      
        currency = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['tradeCode']
        unit_price = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['priceVal']
        quotation_now = get_international_quotation.getInternationalQuotation(currency=currency)
        headers = {"token": mytoken}

        if get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 1:
            if get_ads_info_in_db.judgeIfLimitedPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.sell_fiat_order_limited_jsonString %(repr(ad_ID_NO), 
                repr(advertiser_userid), trade_amount, trade_amount/unit_price, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
            elif get_ads_info_in_db.judgeIfMarketdPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.sell_fiat_order_market_by_amount_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_amount, trade_amount/quotation_now, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
        elif get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 2:
            print('该广告单不是求购广告单')
    except Exception as err:
        print(err)

def sellCurrencyByQuantity(user_name=None, password='123456', ad_ID_NO=None, trade_quantity=None):
    """
    按照数量卖出货币
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        advertiser_userid = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['userId']       
        currency = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['tradeCode']
        unit_price = get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['priceVal']
        quotation_now = get_international_quotation.getInternationalQuotation(currency=currency)
        headers = {"token": mytoken}

        if get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 1:
            if get_ads_info_in_db.judgeIfLimitedPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.sell_fiat_order_limited_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_quantity*unit_price, trade_quantity, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
            elif get_ads_info_in_db.judgeIfMarketdPrice(ad_ID_NO=ad_ID_NO) == True:
                jsonString = get_jsonstring_info.sell_fiat_order_market_by_quantity_jsonString %(repr(ad_ID_NO),
                repr(advertiser_userid), trade_quantity*quotation_now, trade_quantity, repr(currency))
                data = dict(jsonString=jsonString)
                r = requests.post(get_url_info.place_fiat_order_url, data=data, headers=headers)
                print(r.json()['msg'])
                return r.json()['data']['orderId']
        elif get_ads_info_in_db.getAdInfo(ad_ID_NO=ad_ID_NO)[0]['buysell'] == 2:
            print('该广告单不是求购广告单')
    except Exception as err:
        print(err)

if  __name__ == '__main__':
    for i in range(10):
        r = buyCurrencyByAmount(user_name='17727820013@163.com', ad_ID_NO='fa1535333913842187163', trade_amount=500)
        print(r)
        cancel_order.cancelOrder(user_name='17727820013@163.com', order_ID_NO=r)

        r = buyCurrencyByQuantity(user_name='17727820013@163.com', ad_ID_NO='fa1535333913842187163', trade_quantity=100)
        print(r)
        cancel_order.cancelOrder(user_name='17727820013@163.com', order_ID_NO=r)

        r = sellCurrencyByAmount(user_name='17727820013@163.com', ad_ID_NO='fa1535333912905836170', trade_amount=500)
        print(r)
        cancel_order.cancelOrder(user_name='17727820013', order_ID_NO=r)

        r = sellCurrencyByQuantity(user_name='17727820013@163.com', ad_ID_NO='fa1535333912905836170', trade_quantity=50)
        print(r)
        cancel_order.cancelOrder(user_name='17727820013', order_ID_NO=r)    


            

        
            
            
            
            

