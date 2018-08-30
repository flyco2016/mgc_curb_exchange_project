import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import get_ad
import advertising
import init_fund_account_in_db
import get_fund_account
import del_ads_in_db

currency_tuple = ('BYC', 'BTC', 'ETH', 'KBC', 'NZ', 'USDT')
#payment_dict = {"bankcard": 1, "Alipay": 2, "WeChatPay": 4}

def cancelAds(user_name='17727820013', password='123456', ad_ID_NO=None):
    """
    撤销广告
    """
    try:
        mytoken = login(login_num=user_name, password="123456")["data"]["token"]
        jsonString = get_jsonstring_info.cancel_ad_jsonString %(repr(ad_ID_NO))        
        data = dict(jsonString=jsonString)
        headers = {"token": str(mytoken)}
        r = requests.post(get_url_info.cancel_ad_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            print("广告单{0}撤销成功".format(ad_ID_NO))
        else:
            print(r.json()['msg'])
    except Exception as err:
        print(err)

if __name__ == "__main__":
    """
     使用BTC来发布广告，并且再撤销广告，再校验里面的钱对不对
    """
    """
    # 在数据库删除指定用户的广告单
    print('在数据库删除指定用户的广告单......')
    del_ads_in_db.delAdsInDB(currency='BTC')

    # 初始化法币账户的BTC
    print("法币账户BTC初始化中......")
    init_fund_account_in_db.initUserFundAccount(currency='BTC', available_balance=20000, frozen_balance=0)

    # 获取法币资金账户的BTC
    print("获取法币BTC可用余额和冻结金额......")
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("BTC可用余额为：", r['available_balance'])
    print("BTC冻结余额为：", r['frozen_balance'])

    # 发布限价卖出BTC广告10条， 每条1000个BTC
    print("发布限价卖出BTC广告10条， 每条1000个BTC.......")
    for i in range(10):
        advertising.limitedPriceSellAd(currency='BTC', price=1, amount=1000, floor=1, ceiling=1000)

    # 检验BTC可用余额减少10000
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("可用余额为{0}，减少了10000".format(r['available_balance']))
    
    # 检验BTC冻结金额增加10000
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("冻结金额为{0}，增加了10000".format(r['frozen_balance']))
    
    # 发布市价卖出BTC广告10条， 每条1000个BTC
    print("发布限价卖出BTC广告10条， 每条1000个BTC.......")
    for i in range(10):
        advertising.marketPriceSellAd(currency='BTC', amount=1000, floor=1, ceiling=1000)
    
    # 检验BTC可用余额减少10000
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("可用余额为{0}，减少了10000".format(r['available_balance']))
    
    # 检验BTC冻结金额增加10000
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("冻结金额为{0}，增加了10000".format(r['frozen_balance']))
    
    # 获取这些广告单
    ad_list = get_ad.getSellAd(currency='BTC')
    for i in ad_list:
        print(i)

    # 撤销掉所有的卖出BTC的广告
    print('撤销掉所有的卖出BTC的广告')
    for each_item in ad_list:
         cancelAds(ad_ID_NO=each_item)    
    
    # 检验BTC可用余额增加20000
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("可用余额为{0}，增加了20000".format(r['available_balance']))
    
    # 检验BTC冻结金额减少20000
    r = get_fund_account.getFiatFundAccount(currency='BTC')
    print("冻结金额为{0}，减少了20000".format(r['frozen_balance']))
    
    print('检验完毕！')
    """
    ad_list = []
    r1 = get_ad.getBuyAd(currency='NZ')
    r2 = get_ad.getSellAd(currency='NZ')
    ad_list.extend(r1)
    ad_list.extend(r2)

    for i in ad_list:
        cancelAds(ad_ID_NO = i)
