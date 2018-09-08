import requests
import get_token
from utils import get_url_info
from utils import get_jsonstring_info

def applyForMerchantInPC(user_name='17727820013', login_password='123456', nickname=None):
    """
    函数功能：在PC端申请为商家
    """
    try:
        mytoken = get_token.getToken(user_name=user_name, password=login_password)
        jsonString = get_jsonstring_info.apply_for_merchant_in_PC_jsongString %(repr(nickname))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.apply_for_merchant_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print('提交商家申请成功')
        else:
            print(r.json()['msg'])  
    except Exception as err:
        print(err)

def applyForMerchantInAndroid(user_name='17727820013', login_password='123456', nickname=None):
    try:
        mytoken = get_token.getToken(user_name=user_name, password=login_password)
        jsonString = get_jsonstring_info.apply_for_merchant_in_Android_jsongString %(repr(nickname))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.apply_for_merchant_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print('提交商家申请成功')
        else:
            print(r.json()['msg'])   
    except Exception as err:
        print(err)
    
def applyForMerchantInIOS(user_name='17727820013', login_password='123456', nickname=None):
    try:
        mytoken = get_token.getToken(user_name=user_name, password=login_password)
        jsonString = get_jsonstring_info.apply_for_merchant_in_IOS_jsongString %(repr(nickname))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.apply_for_merchant_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print('提交商家申请成功')
        else:
            print(r.json()['msg'])  
    except Exception as err:
        print(err)

if __name__ == '__main__':
    import random
    import init_fund_account_in_db
    #applyForMerchantInPC(nickname='案例三等奖')
    # 准备用户数据
    phone_user_list = ['1772781000{}'.format(i) for i in range(5)] 
    email_user_list = ['1772781000{}@163.com'.format(i) for i in range(5)]
    phone_user_list.extend(email_user_list)
    total_user_list = phone_user_list
    method_list = [applyForMerchantInPC, applyForMerchantInAndroid, applyForMerchantInIOS]
    
    # 初始化NZ的账户
    for user in total_user_list:
        init_fund_account_in_db.initUserFundAccount(user_nickname=user, currency='NZ', available_balance=100000, frozen_balance=0)
    
    # 随机申请商家
    i = 0
    for user in total_user_list:
        """
        random.choice(method_list)(user_name=user, login_password='abc123456', 
        nickname='商家{}'.format(str(random.sample([i for i in range(1, 11)], 1)[0])))
        """
        random.choice(method_list)(user_name=user, login_password='abc123456', 
        nickname='商家{}(批量)'.format(str(i+1)))
        i = i + 1
