import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import get_ad_status, get_order_status
import cancel_order

def markAsPayment(buyer_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：买家标记订单为付款
    """
    try:
        if (get_order_status.getOrderStatus(user_name=buyer_user_name, order_ID_NO=order_ID_NO)['order_status']
            not in [2, 3, 4, 5, 6]):
            mytoken = login(login_num=buyer_user_name, password=password)["data"]["token"]
            jsonString = get_jsonstring_info.update_fiat_order_jsonString %(repr(order_ID_NO))        
            data = dict(jsonString=jsonString)
            headers = {"token": str(mytoken)}
            r = requests.post(get_url_info.update_fiat_order_url, data=data, headers=headers)
            if r.json()['msg'] == '操作完成':
                print('订单{0}标记为付款成功'.format(order_ID_NO))
            else:
                print(r.json()['msg'])
        else:
            print('无法标记为已付款')
    except Exception as err:
        print(err)

def markAsReceipt(seller_user_name=None, password='123456', order_ID_NO=None):
    """
    函数功能：卖家标记订单为收款
    """
    try:
        if (get_order_status.getOrderStatus(user_name=seller_user_name, order_ID_NO=order_ID_NO)['order_status']
            not in [1, 3, 4, 5, 6]):
            mytoken = login(login_num=seller_user_name, password=password)["data"]["token"]
            jsonString = get_jsonstring_info.update_fiat_order_jsonString %(repr(order_ID_NO))        
            data = dict(jsonString=jsonString)
            headers = {"token": str(mytoken)}
            r = requests.post(get_url_info.update_fiat_order_url, data=data, headers=headers)
            if r.json()['msg'] == '操作完成':
                print('订单{0}标记收款成功'.format(order_ID_NO))
            else:
                print(r.json()['msg'])
        else:
            print('无法标记为已收款')
    except Exception as err:
        print(err)   

if __name__ == '__main__':
    markAsPayment(buyer_user_name='17727820013', order_ID_NO='1536126027925172837')
    cancel_order.cancelOrder(buyer_user_name='17727820013', order_ID_NO='1536126027925172837')
    markAsReceipt(seller_user_name='17727820013@163.com', order_ID_NO='1536126027925172837') 