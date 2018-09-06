import requests
from utils import get_url_info
from utils import get_jsonstring_info
import send_authcode

def registerByPhoneThroughPC(phone=None, password=None):
    """
    函数功能：通过手机号PC注册
    """
    try:
        jsonString = get_jsonstring_info.register_through_PC_jsonString %(repr(phone), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendPhoneAuthcode(phone=phone, device=1)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("手机注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByPhoneThroughIOS(phone=None, password=None):
    """
    函数功能：通过手机号IOS注册
    """
    try:
        jsonString = get_jsonstring_info.register_through_IOS_jsonString %(repr(phone), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendPhoneAuthcode(phone=phone, device=3)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("手机注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByPhoneThroughAndroid(phone=None, password=None):
    """
    函数功能：通过手机号安卓注册
    """
    try:
        jsonString = get_jsonstring_info.register_through_Android_jsonString %(repr(phone), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendPhoneAuthcode(phone=phone, device=2)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("手机注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByPhoneThroughH5WithInviterCode(phone=None, password=None, inviter_code=None):
    """
    函数功能：通过手机号H5注册(带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_with_inviterCode_jsonString %(repr(phone), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendPhoneAuthcode(phone=phone, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("手机注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByPhoneThroughH5WithoutInviterCode(phone=None, password=None, inviter_code=None):
    """
    函数功能：通过手机号H5注册(不带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_without_inviterCode_jsonString %(repr(phone), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendPhoneAuthcode(phone=phone, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("手机注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughPC(email=None, password=None):
    """
    函数功能：通过邮箱PC注册
    """
    try:
        jsonString = get_jsonstring_info.register_through_PC_jsonString %(repr(email), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=1)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("邮箱注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughIOS(email=None, password=None):
    """
    函数功能：通过邮箱IOS注册
    """
    try:
        jsonString = get_jsonstring_info.register_through_IOS_jsonString %(repr(email), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=3)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("邮箱注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughAndroid(email=None, password=None):
    """
    函数功能：通过手机号安卓注册
    """
    try:
        jsonString = get_jsonstring_info.register_through_Android_jsonString %(repr(email), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=2)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("邮箱注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughH5WithInviterCode(email=None, password=None, inviter_code=None):
    """
    函数功能：通过邮箱H5注册(带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_with_inviterCode_jsonString %(repr(email), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("邮箱注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughH5WithoutInviterCode(email=None, password=None, inviter_code=None):
    """
    函数功能：通过邮箱H5注册(不带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_without_inviterCode_jsonString %(repr(email), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("邮箱注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

if __name__ == '__main__':
    import random
    import string
    """
    检验在某个手机段范围内的注册，密码使用随机8位密码
    """
    """
    for i in range(17727820078, 17727820080):
        registerByPhoneThroughPC(phone=str(i), password=''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 8)))
    """
    registerByPhoneThroughIOS(phone='17727820089', password='abc123456')
    registerByPhoneThroughAndroid(phone='17727820090', password='abc123456')
    

