import requests
from utils import get_url_info
from utils import get_jsonstring_info

def sendPhoneAuthcode(phone=None, device=None):
    try:
        jsonString = get_jsonstring_info.send_phone_authcode_jsonString %(repr(phone), device)
        r = requests.post(get_url_info.send_phone_authcode_url, data=dict(jsonString=jsonString))
        if r.json()['msg'] == '操作完成':
            pass
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

def sendEmailAuthcode(email=None, device=None):
    try:
        jsonString = get_jsonstring_info.send_email_authcode_jsonString %(repr(email), device)
        r = requests.post(get_url_info.send_email_authcode_url, data=dict(jsonString=jsonString))
        if r.json()['msg'] == '操作完成':
            pass
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)


if __name__ == '__main__':

    sendPhoneAuthcode(phone='17727820013', device=1)
    sendPhoneAuthcode(phone='17727820013', device=2)
    sendPhoneAuthcode(phone='17727820013', device=3)
    sendPhoneAuthcode(phone='17727820013', device=4)
    
    sendEmailAuthcode(email='17727820013@163.com', device=1)
    sendEmailAuthcode(email='17727820013@163.com', device=2)
    sendEmailAuthcode(email='17727820013@163.com', device=3)
    sendEmailAuthcode(email='17727820013@163.com', device=4)


