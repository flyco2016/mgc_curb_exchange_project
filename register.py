import requests
from utils import get_url_info
from utils import get_jsonstring_info
import send_authcode
from del_user_info_in_db import quickToDel
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
            print("通过手机号PC注册成功," + r.json()['msg'])
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
            print("通过手机号IOS注册成功," + r.json()['msg'])
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
            print("通过手机号安卓注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByPhoneThroughH5WithInviterCode(phone=None, password=None, inviter_code=None):
    """
    函数功能：通过手机号H5注册(带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_with_inviterCode_jsonString %(repr(phone), repr(password), repr(inviter_code))        
        data = dict(jsonString=jsonString)
        send_authcode.sendPhoneAuthcode(phone=phone, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("通过手机号H5注册(带邀请码)成功," + r.json()['msg'])
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
            print("通过手机号H5注册(不带邀请码)成功," + r.json()['msg'])
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
            print("通过邮箱PC注册成功," + r.json()['msg'])
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
            print("通过邮箱IOS注册成功," + r.json()['msg'])
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
            print("通过手机号安卓注册成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughH5WithInviterCode(email=None, password=None, inviter_code=None):
    """
    函数功能：通过邮箱H5注册(带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_with_inviterCode_jsonString %(repr(email), repr(password), repr(inviter_code))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("通过邮箱H5注册(带邀请码)成功," + r.json()['msg'])
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def registerByEmailThroughH5WithoutInviterCode(email=None, password=None):
    """
    函数功能：通过邮箱H5注册(不带邀请码)
    """
    try:
        jsonString = get_jsonstring_info.register_through_H5_without_inviterCode_jsonString %(repr(email), repr(password))        
        data = dict(jsonString=jsonString)
        send_authcode.sendEmailAuthcode(email=email, device=4)
        r = requests.post(get_url_info.register_url, data=data)
        if r.json()['code'] == 1:
            print("通过邮箱H5注册(不带邀请码)成功," + r.json()['msg'])
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
    # 删除原来的
    #quickToDel()

    # 手机方式注册测试
    registerByPhoneThroughPC(phone='17727810000', password='abc123456')
    registerByPhoneThroughIOS(phone='17727810001', password='abc123456')
    registerByPhoneThroughAndroid(phone='17727810002', password='abc123456')
    registerByPhoneThroughH5WithInviterCode(phone='17727810003', password='abc123456', inviter_code='94uH58')
    registerByPhoneThroughH5WithoutInviterCode(phone='17727810004', password='abc123456')

    # 邮箱方式注册测试
    registerByEmailThroughPC(email='17727810000@163.com', password='abc123456')
    registerByEmailThroughIOS(email='17727810001@163.com', password='abc123456')
    registerByEmailThroughAndroid(email='17727810002@163.com', password='abc123456')
    registerByEmailThroughH5WithInviterCode(email='17727810003@163.com', password='abc123456', inviter_code='94uH58')
    registerByEmailThroughH5WithoutInviterCode(email='17727810004@163.com', password='abc123456')


