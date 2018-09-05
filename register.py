import requests
import json
import random


def bat_reg_telephone_user(tele_lower_limit, tele_upper_limit):
    """
    author:tengfei Ma
    purpose:注册n个账户,两个参数为上限和下限
    input_type:int
    return_type:list
    """
    base_url = 'http://192.168.13.221:8021/api/'
    reg_url = base_url + 'user/userRegister'
    reg_list = []
    
    for tele in range(tele_lower_limit, tele_upper_limit):
        value_str = """{
        "device": %d,
        "loginNum": %s,
        "password": "abc123456",
        "code": "989899",
        "regFromCode": "86"
        }""" % (random.randint(1, 4), repr(tele))   # 生成随机注册端还有随机注册号码的值  
        r = requests.post(reg_url, data=dict(jsonString=value_str))
        reg_list.append(r.json())
    return reg_list

if __name__ == '__main__':
    user_list = bat_reg_telephone_user(15071458530, 15071458540)
    for i in user_list:
        print(i)
