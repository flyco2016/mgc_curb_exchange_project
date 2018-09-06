import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info

def sellerAppealThroughBank(seller_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：卖家通过银行卡信息申诉
    """
    try:
        mytoken = login(login_num=seller_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.seller_appeal_through_bank_jsonString %(repr(order_ID_NO),
        repr(order_ID_NO))
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.appeal_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
       print(err)

def sellerAppealThroughAlipay(seller_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：卖家通过支付宝信息申诉
    """
    try:
        mytoken = login(login_num=seller_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.seller_appeal_through_Alipay_jsonString %(repr(order_ID_NO),
        repr(order_ID_NO))
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.appeal_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
       print(err)

def sellerAppealThroughWechat(seller_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：卖家通过微信信息申诉
    """
    try:
        mytoken = login(login_num=seller_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.seller_appeal_through_Wechat_jsonString %(repr(order_ID_NO),
        repr(order_ID_NO))
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.appeal_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
       print(err)

def buyerAppealThroughBank(buyer_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：买家通过银行卡信息申诉
    """
    try:
        mytoken = login(login_num=buyer_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.buyer_appeal_through_bank_jsonString %(repr(order_ID_NO),
        repr(order_ID_NO))
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.appeal_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
       print(err)

def buyerAppealThroughAlipay(buyer_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：买家通过支付宝信息申诉
    """
    try:
        mytoken = login(login_num=buyer_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.buyer_appeal_through_Alipay_jsonString %(repr(order_ID_NO),
        repr(order_ID_NO))
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.appeal_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
       print(err)

def buyerAppealThroughWechat(buyer_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：买家通过微信信息申诉
    """
    try:
        mytoken = login(login_num=buyer_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.buyer_appeal_through_Wechat_jsonString %(repr(order_ID_NO),
        repr(order_ID_NO))
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.appeal_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
       print(err)

if __name__ == "__main__":
    sellerAppealThroughBank(seller_user_name='17727820013@163.com', order_ID_NO='1536132964574021461')
    buyerAppealThroughWechat(buyer_user_name='17727820013', order_ID_NO='1536132964574021461')