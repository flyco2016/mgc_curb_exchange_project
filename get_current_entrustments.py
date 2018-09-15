import requests
from get_token import getToken
from utils import get_url_info
from utils import get_jsonstring_info


def getMyCurrentEntrustmentsInPC(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ'):
    """
    函数功能：在PC上获取当前委托
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.get_current_entrustments_in_PC_jsonString %(repr(symbol), repr(market))
    data = dict(jsonString=jsonString)
    headers = {"token": mytoken}
    r = requests.post(get_url_info.get_current_entrustments_url, data=data, headers=headers)
    print(r.json())

def getMyCurrentEntrustmentsInAndroid(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ'):
    """
    函数功能：在安卓上获取当前委托
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.get_current_entrustments_in_Android_jsonString %(repr(symbol), repr(market))
    data = dict(jsonString=jsonString)
    headers = {"token": mytoken}
    r = requests.post(get_url_info.get_current_entrustments_url, data=data, headers=headers)
    print(r.json())

def getMyCurrentEntrustmentsInIOS(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ'):
    """
    函数功能：在IOS上获取当前委托
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.get_current_entrustments_in_IOS_jsonString %(repr(symbol), repr(market))
    data = dict(jsonString=jsonString)
    headers = {"token": mytoken}
    r = requests.post(get_url_info.get_current_entrustments_url, data=data, headers=headers)
    print(r.json())


if __name__ == "__main__":
    getMyCurrentEntrustmentsInPC()
    #getMyCurrentEntrustmentsInIOS()
    #getMyCurrentEntrustmentsInAndroid()
