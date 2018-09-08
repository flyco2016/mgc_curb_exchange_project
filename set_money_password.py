import requests
import get_token
from utils import get_url_info
from utils import get_jsonstring_info

def setMoneyPasswordInPC(user_name='17727820013', login_password='123456', new_money_password=None):
    """
    函数功能：在PC端设置资金密码
    """
    try:
        mytoken = get_token.getToken(user_name=user_name, password=login_password)
        jsonString = get_jsonstring_info.set_money_password_in_PC_jsonString %(repr(user_name), repr(new_money_password))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.money_password_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print('PC端设置资金密码成功')
        else:
            print('无法设置资金密码，' + r.json()['msg'])
    except Exception as err:
        print(err)

def setMoneyPasswordInAndroid(user_name='17727820013', login_password='123456', new_money_password=None):
    """
    函数功能：在安卓端设置资金密码
    """
    try:
        mytoken = get_token.getToken(user_name=user_name, password=login_password)
        jsonString = get_jsonstring_info.set_money_password_in_Android_jsonString %(repr(user_name), repr(new_money_password))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.money_password_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print('安卓端设置资金密码成功')
        else:
            print('无法设置资金密码，' + r.json()['msg'])
    except Exception as err:
        print(err)

def setMoneyPasswordInIOS(user_name='17727820013', login_password='123456', new_money_password=None):
    """
    函数功能：在IOS端设置资金密码
    """
    try:
        mytoken = get_token.getToken(user_name=user_name, password=login_password)
        jsonString = get_jsonstring_info.set_money_password_in_IOS_jsonString %(repr(user_name), repr(new_money_password))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.money_password_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print('IOS端设置资金密码成功')
        else:
            print('无法设置资金密码，' + r.json()['msg'])
    except Exception as err:
        print(err)

if __name__ == "__main__":
    setMoneyPasswordInPC(new_money_password='abc123456')
    setMoneyPasswordInAndroid(new_money_password='abc123456')
    setMoneyPasswordInIOS(new_money_password='abc123456')
    