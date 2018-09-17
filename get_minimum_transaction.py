import requests
from utils import get_url_info
from utils import get_jsonstring_info


def getMinimumTrancsaction(currency='BTC'):
    """
    函数功能：获取币种最小交易量
    输入参数：currency---币种
    输出参数：最小交易量（float）
    """
    r = requests.post(get_url_info.get_minimum_transaction_url)
    if (r.json()['msg']=='操作完成') and (len(r.json()['data'])>0):
        for i in r.json()['data']:
            if i['tradeCode'] == currency:
                return i['minVolume']
    else:
        print(r.json()['msg'])
            

if __name__ == "__main__":
    print(getMinimumTrancsaction(currency='NZ'))