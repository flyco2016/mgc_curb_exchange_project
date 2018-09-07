import requests
import random
from utils import get_url_info
from utils import get_jsonstring_info


def login(login_num='17727820013@163.com', password='123456'):
    """
    函数功能：随机设备登录
    """
    try:
        jsonString = get_jsonstring_info.login_jsonString % (random.randint(1, 3), repr(login_num), repr(password))
        r = requests.post(get_url_info.login_url, data=dict(jsonString=jsonString))
        return r.json() 
    except Exception as err:
        print(err)

def loginByPC(login_num='17727820013@163.com', password='123456'):
    """
    函数功能：PC端登录
    输入参数：
    login_num---登录账号
    password---登录密码
    返回参数：
    token
    """
    try:
        jsonString = get_jsonstring_info.login_jsonString % (1, repr(login_num), repr(password))
        r = requests.post(get_url_info.login_url, data=dict(jsonString=jsonString))
        if r.json()['msg'] == '操作完成':
            return r.json()['data']['token']
        else:
            print(r.json()['msg']) 
    except Exception as err:
        print(err)

def loginByIOS(login_num='17727820013@163.com', password='123456'):
    """
    函数功能：IOS端登录
    """
    try:
        jsonString = get_jsonstring_info.login_jsonString % (3, repr(login_num), repr(password))
        r = requests.post(get_url_info.login_url, data=dict(jsonString=jsonString))
        if r.json()['msg'] == '操作完成':
            return r.json()['data']['token']
        else:
            print(r.json()['msg']) 
    except Exception as err:
        print(err)

def loginByAndroid(login_num='17727820013@163.com', password='123456'):
    """
    函数功能：安卓端登录
    """
    try:
        jsonString = get_jsonstring_info.login_jsonString % (2, repr(login_num), repr(password))
        r = requests.post(get_url_info.login_url, data=dict(jsonString=jsonString))
        if r.json()['msg'] == '操作完成':
            return r.json()['data']['token']
        else:
            print(r.json()['msg']) 
    except Exception as err:
        print(err)

if __name__ == "__main__":
    """
    测试数据，通过修改数据库用户的登录
    密码，然后再登录
    """
    #db = mydb.MyDB()
    #sql = "UPDATE User SET password = '123456' WHERE userId = 'c0caded4-42d8-447b-a3cc-1c00164f4dfd'"
    #db.update_data_in_db(sql)
    """
    for i in range(10):
        r = login(login_num='17727820013@163.com', password='123456')
        print(r)
    """
    for i in [loginByAndroid, loginByIOS, loginByPC]:
        print(i())