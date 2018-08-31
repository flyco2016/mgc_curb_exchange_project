import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info

def getAdStatus(user_name='17727820013', password='123456', ad_ID_NO=None):
    try:
        temp_list = []
        for each_item in range(20):
            mytoken = login(login_num=user_name, password=password)["data"]["token"]
            jsonString = get_jsonstring_info.get_single_ad_jsonString %(repr(ad_ID_NO), each_item)        
            data = dict(jsonString=jsonString)
            headers = {"token": mytoken}
            r = requests.post(get_url_info.get_ad_list_url, data=data, headers=headers)
            if (r.json()['msg'] == '操作完成') and (len(r.json()['data']['list']) != 0):
                temp_list.append(r.json())
        temp_data = temp_list['data']['list'][0]
        result_dict = dict(currency=temp_data['tradeCode'], 
                           order_status=temp_data['orderStatus'],
                           quantity_completion=temp_data['completionOrderVal'],
                           limited_or_market=temp_data['type'],
                           user_ID=temp_data['userId'],
                           buy_or_sell=temp_data['buysell'],
                           floor=temp_data['lowVal'],
                           ceilling=temp_data['hightVal'],
                           payment_support=temp_data['payVal'],
                           frozen_or_unfrozen=temp_data['frozenStatus'],
                           frozen_quantity=temp_data['frozenOrderVal'],
                           remaining_quantity=temp_data['remainOrderNumber'],
                           advertising_time=temp_data['advertisingTime']
                           )
        return result_dict
    except Exception as err:
        print(err)


if __name__ == '__main__':
    r = getAdStatus(ad_ID_NO='fa1535506797251355446')
    for i, j in r.items():
        print(i, '=', j)


        
