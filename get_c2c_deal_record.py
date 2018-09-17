import requests
from utils import get_url_info
from utils import get_jsonstring_info


def getC2CDealRecord(symbol='BTC', market='NZ'):
    """
    函数功能：获取币币最新成交记录
    """
    jsonString = get_jsonstring_info.get_c2c_deal_record_jsonString %(repr(symbol), repr(market))
    data = dict(jsonString=jsonString)
    r = requests.post(get_url_info.get_c2c_deal_record_url, data=data)
    if r.json()['msg'] == '操作完成':
        print(r.json()['data'])
    else:
        print(r.json()['msg'])


if __name__ == "__main__":
    getC2CDealRecord()