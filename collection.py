import requests
from get_token import getToken
from utils import get_url_info
from utils import get_jsonstring_info



def addCollection(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ'):
    """
    函数功能：添加自选交易对
    """
    transpare = symbol + ':' + market
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.add_collection_jsonString %(repr(transpare))
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.add_collection_url, data=data, headers=headers)
    if (r.json()['msg'] == '操作完成') and (r.json()['data'] != None):
        print('交易对{symbol}:{market}添加自选成功'.format(symbol=symbol, market=market))
        return r.json()['data']
    else:
        print('交易对{symbol}:{market}添加自选失败'.format(symbol=symbol, market=market))

def delCollection(user_name='17727820013', password='123456', symbol='BTC', 
market='NZ'):
    """
    函数功能：删除自选交易对
    """
    transpare = symbol + ':' + market
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.del_collection_jsonString %(repr(transpare))
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.del_collection_url, data=data, headers=headers)
    if (r.json()['msg'] == '操作完成'):
        print('交易对{symbol}:{market}删除自选成功'.format(symbol=symbol, market=market))
        return r.json()['data']
    else:
        print(r.json())

def getCollectionInPC(user_name='17727820013', password='123456'):
    """
    函数功能：在PC上获取自选交易对
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.get_collection_in_PC_jsonString
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.get_collection_url, data=data, headers=headers)
    if (r.json()['msg'] == '操作完成') and (len(r.json()['data']) > 0):
        return r.json()['data']
    else:
        print(r.json())

def getCollectionInAndroid(user_name='17727820013', password='123456'):
    """
    函数功能：在PC上获取自选交易对
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.get_collection_in_Android_jsonString
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.get_collection_url, data=data, headers=headers)
    if (r.json()['msg'] == '操作完成') and (len(r.json()['data']) > 0):
        return r.json()['data']
    else:
        print(r.json())

def getCollectionInIOS(user_name='17727820013', password='123456'):
    """
    函数功能：在PC上获取自选交易对
    """
    mytoken = getToken(user_name=user_name, password=password)
    jsonString = get_jsonstring_info.get_collection_in_IOS_jsonString
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.get_collection_url, data=data, headers=headers)
    if (r.json()['msg'] == '操作完成') and (len(r.json()['data']) > 0):
        return r.json()['data']
    else:
        print(r.json())


if __name__ == "__main__":
    #addCollection(symbol='OWN')
    #delCollection(symbol='OWN')
    print(getCollectionInPC())
    print(getCollectionInAndroid())
    print(getCollectionInIOS())