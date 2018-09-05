import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info


def cancelOrder(buyer_user_name='17727820013', password='123456', order_ID_NO=None):
    """
    取消订单
    """
    try:
        mytoken = login(login_num=buyer_user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.cancel_order_jsonString %(repr(order_ID_NO))        
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.cancel_order_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print("法币订单{0}取消成功".format(order_ID_NO))
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

if __name__ == "__main__":
    cancelOrder(buyer_user_name='17727820013', order_ID_NO='1535442831587410665')
