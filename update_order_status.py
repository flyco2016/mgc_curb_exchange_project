import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import get_ad_status, get_order_status

def markAsPayment(buyer_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：标记订单已经付款
    """
    try:
        if (get_order_status.getOrderStatus(user_name=buyer_user_name, order_ID_NO=order_ID_NO)['order_status']
            not in [2, 3, 4, 5, 6]):
            mytoken = login(login_num=buyer_user_name, password=password)["data"]["token"]
            jsonString = get_jsonstring_info.update_fiat_order_jsonString %(repr(order_ID_NO))        
            data = dict(jsonString=jsonString)
            headers = {"token": str(mytoken)}
            r = requests.post(get_url_info.update_fiat_order_url, data=data, headers=headers)
            print(r.json()['msg'])
        else:
            print('无法标记为已付款')
    except Exception as err:
        print(err)

def markAsReceipt(seller_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：标记订单已经收款
    """
    try:
        if (get_order_status.getOrderStatus(user_name=seller_user_name, order_ID_NO=order_ID_NO)['order_status']
            not in [1, 3, 4, 5, 6]):
            mytoken = login(login_num=seller_user_name, password=password)["data"]["token"]
            jsonString = get_jsonstring_info.update_fiat_order_jsonString %(repr(order_ID_NO))        
            data = dict(jsonString=jsonString)
            headers = {"token": str(mytoken)}
            r = requests.post(get_url_info.update_fiat_order_url, data=data, headers=headers)
            print(r.json()['msg'])
        else:
            print('无法标记为已收款')
    except Exception as err:
        print(err)   

def markAsCancel(seller_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：标记订单为取消
    """
    try:
        if (get_order_status.getOrderStatus(user_name=seller_user_name, order_ID_NO=order_ID_NO)['order_status']
            not in [1, 3, 4, 5, 6]):
            mytoken = login(login_num=seller_user_name, password=password)["data"]["token"]
            jsonString = get_jsonstring_info.update_fiat_order_jsonString %(repr(order_ID_NO))        
            data = dict(jsonString=jsonString)
            headers = {"token": str(mytoken)}
            r = requests.post(get_url_info.update_fiat_order_url, data=data, headers=headers)
            print(r.json())
        else:
            print('无法标记为已收款')
    except Exception as err:
        print(err)



if __name__ == '__main__':
    for i in range(2):
        markAsPayment(buyer_user_name='17727820013', order_ID_NO='1535979259612489838')
        markAsReceipt(seller_user_name='17727820013@163.com', order_ID_NO='1535979259612489838')