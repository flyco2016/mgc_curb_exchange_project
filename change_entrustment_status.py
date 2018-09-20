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
    if r.json()['msg'] == "操作完成":
        print('{}撤单完成'.format(entrustment_ID))
    else:
        print(r.json())

if __name__ == "__main__":
    import get_current_entrustments
    import get_buy_and_sell_five_gears
    import time
    import threading

    # 撤销自己的当前委托单
    old_time = time.time()
    count = 0
    for j in [i['id'] for i in get_current_entrustments.getMyCurrentEntrustmentsInAndroid(symbol='BTC', market='NZ')]:
        t = threading.Thread(target=cancelEntrustment, kwargs={'entrustment_ID':j})
        t.start()
        count += 1
    print('总计撤单为{}'.format(count))
    #print('总计撤单耗时{}'.sleep(time.time()-old_time))
    
    """
    # 买卖五档应该清空
    print(get_buy_and_sell_five_gears.getBuyFiveGears())
    print(get_buy_and_sell_five_gears.getSellFiveGears())
    """