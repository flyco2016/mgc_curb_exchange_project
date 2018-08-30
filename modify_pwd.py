import requests
import login
from utils import get_url_info
from utils import get_jsonstring_info


def mod_pwd(user=None, old_pwd=None, new_pwd=None):
    try:
        jsonString = get_jsonstring_info.modifypwd_jsonString %(repr(old_pwd), repr(new_pwd), 2)
        mytoken = login.login(loginNum=user, password=old_pwd)["data"]["token"]
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        if (old_pwd == None) or (new_pwd == None):
            print("pls input your new password!")
        else:
            r = requests.post(get_url_info.modifypwd_url, data=data, headers=headers)
            if r.json()['msg'] == '操作完成':
                print('modify successfully!')
            else:
                print(r.json()['msg'])
    except Exception as err:
        print(err)

if __name__ == "__main__":
    #mod_pwd(user="17727820013", old_pwd='123456', new_pwd='123456')  # 密码相同的检验
    #mod_pwd(user="17727820013", old_pwd='123456', new_pwd='abc123456')  # 密码修改成功
    mod_pwd(user="17727820013", old_pwd='123456', new_pwd='abc123456')  # 旧密码错误
