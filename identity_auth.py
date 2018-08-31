import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info

def IDcardIdentity(user_name=None, password='123456', full_name=None, ID_card_NO=None):
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.identity_IDcard_jsonString %(repr(full_name), repr(ID_card_NO))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.identity_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
        print(err)
    

def passportIdentity(user_name=None, password='123456', ID_card_NO=None, 
    surname=None, name=None):
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.identity_passport_jsonString %(repr(ID_card_NO), repr(surname),
        repr(name))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.identity_url, data=data, headers=headers)
        print(r.json()['msg'])
    except Exception as err:
        print(err)

if __name__ == "__main__":
    # 测试身份证认证
    IDcardIdentity(user_name='17727820013@163.com', password='123456', 
    ID_card_NO="45213219910302", full_name="马腾飞")
    
    # 测试护照认证
    passportIdentity(user_name='17727820013', password='123456', 
    ID_card_NO='12345623', surname='马', name='腾飞')




    
