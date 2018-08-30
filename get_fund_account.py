import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info


def getFiatFundAccount(user_name='17727820013', password='123456', currency=None):
    """
    获取法币某个币种的资金账户可用余额还有冻结余额
    """
    try:
        fiat_fund_dict = {}
        mytoken = login(loginNum=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.get_fiat_fund_account_jsonString %(repr(currency))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.get_fiat_fund_account_url, data=data, headers=headers)
        fiat_fund_dict.update(available_balance=r.json()['data']['ufflist'][0]['availableBalance'], 
        frozen_balance=r.json()['data']['ufflist'][0]['frozenBalance'], 
        RMB_valuation = r.json()['data']['cnySum'])
        return fiat_fund_dict
    except Exception as err:
        print(err)

def getCoinFundAccount(user_name='17727820013', password='123456', currency=None):
    """
    获取法币某个币种的资金账户可用余额还有冻结余额
    """
    try:

        coin_fund_dict = {}
        mytoken = login(loginNum=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.get_coin_fund_account_jsonString %(repr(currency))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.get_coin_fund_account_url, data=data, headers=headers)
        coin_fund_dict.update(available_balance=r.json()['data']['ufflist'][0]['availableBalance'], 
        frozen_balance=r.json()['data']['ufflist'][0]['frozenBalance'], 
        RMB_valuation = r.json()['data']['cnySum'])
        return coin_fund_dict
    except Exception as err:
        print(err)

if __name__ == '__main__':
    print(getFiatFundAccount(currency='BTC')['available_balance'])
    print(getFiatFundAccount(currency='BTC')['frozen_balance'])
    print(getFiatFundAccount(currency='BTC')['RMB_valuation'])
    print(getCoinFundAccount(currency='BTC')['available_balance'])
    print(getCoinFundAccount(currency='BTC')['frozen_balance'])
    print(getCoinFundAccount(currency='BTC')['RMB_valuation'])
    