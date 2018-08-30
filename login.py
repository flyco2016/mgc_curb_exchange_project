import requests
import json
from utils import mydb
import register
import random
from utils import get_url_info
from utils import get_jsonstring_info


def login(login_num=None, password=None):
    """
    实现登陆功能，返回json格式数据，便于后面调用
    """
    try:
        jsonString = get_jsonstring_info.login_jsonString % (random.randint(1, 3), repr(login_num), repr(password))
        r = requests.post(get_url_info.login_url, data=dict(jsonString=jsonString))
        return r.json() 
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
    for i in range(10):
        r = login(login_num='17727820013@163.com', password='123456')
        print(r)
