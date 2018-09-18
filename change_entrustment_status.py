import requests
from get_token import getToken
from utils import get_url_info
from utils import get_jsonstring_info


def cancelEntrustment(user_name='17727820013', password='123456', entrustment_ID=None):
    """
    函数功能：撤销委托单
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.cancel_entrustment_jsonSring %(repr(entrustment_ID))
    data = dict(jsonString=jsonString)
    headers = {"token": mytoken}
    r = requests.post(get_url_info.update_entrustment_status_url, data=data, headers=headers)
    print(r.json())

if __name__ == "__main__":
    import get_current_entrustments
    import get_buy_and_sell_five_gears
    
    # 撤销自己的当前委托单
    for j in [i['id'] for i in get_current_entrustments.getMyCurrentEntrustmentsInAndroid()]:
        cancelEntrustment(entrustment_ID=j)
    
    # 买卖五档应该清空
    print(get_buy_and_sell_five_gears.getBuyFiveGears())
    print(get_buy_and_sell_five_gears.getSellFiveGears())