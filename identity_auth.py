import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info

def IDcardIdentity(user_name=None, password=None, full_name=None, ID_card_NO=None):
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.identity_IDcard_jsonString %(repr(full_name), repr(ID_card_NO))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.identity_url, data=data, headers=headers)
        print(r.json())
    except Exception as err:
        print(err)
    

def passportIdentity(user_name=None, password=None, ID_card_NO=None, 
    surname=None, name=None):
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.identity_IDcard_jsonString %(repr(ID_card_NO),repr(surname),
        repr(name))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.identity_url, data=data, headers=headers)
        print(r.json())
    except Exception as err:
        print(err)

if __name__ == "__main__":
    IDcardIdentity(user_name='17727820013@163.com', password='123456', 
    ID_card_NO="123456789", full_name="马腾飞")




    
