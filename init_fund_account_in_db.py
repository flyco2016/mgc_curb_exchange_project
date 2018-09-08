from utils import mydb


fiat_currency_tuple = ('BTC', 'ETH', 'KBC', 'NZ', 'USDT')
c2c_currency_tuple = ()

def initUserFundAccount(fund_type='UserFiatFunds', user_nickname='手机商家', currency=None, available_balance=None, frozen_balance=None):
    """
    函数名：initUserFundAccount
    函数功能：初始化资金账户
    输入参数：
    fund_type---资金账户类型
    user_nickname---用户昵称，如果是商家则是商家自己的名字，如果不是则是手机或者邮箱
    currency---币种代号
    available_balance---可用余额
    frozen_balance---冻结余额
    输出参数：
    无
    """
    try:
        db = mydb.MyDB()

        user_sql = """SELECT * 
                      FROM User 
                      WHERE nikeName = {0};""".format(repr(user_nickname))
        user_id = db.fetch_data_from_db(user_sql)[0]["userId"]
        
        if (currency != "all"):
            if (available_balance == None):
                update_sql = """UPDATE {3} 
                                SET frozenBalance = {0} 
                                WHERE userId = {1} 
                                AND tradeCode = {2};""".format(frozen_balance, repr(user_id), repr(currency), fund_type)
                db.update_data_in_db(update_sql)
            elif (frozen_balance == None):
                update_sql = """UPDATE {3} 
                                SET availableBalance = {0} 
                                WHERE userId = {1} 
                                AND tradeCode = {2};""".format(available_balance, repr(user_id), repr(currency), fund_type)
                db.update_data_in_db(update_sql)
            else:
                update_sql = """UPDATE {4} 
                                SET availableBalance = {0}, frozenBalance = {1} 
                                WHERE userId = {2} 
                                AND tradeCode = {3};""".format(available_balance, frozen_balance, repr(user_id), repr(currency), fund_type)
                db.update_data_in_db(update_sql)
        elif (currency == 'all'):
            if (available_balance == None):
                update_sql = """UPDATE {2} 
                                SET frozenBalance = {0} 
                                WHERE userId = {1};""".format(frozen_balance, repr(user_id), fund_type)
                db.update_data_in_db(update_sql)
            elif (frozen_balance == None):
                update_sql = """UPDATE {2} 
                                SET availableBalance = {0} 
                                WHERE userId = {1};""".format(available_balance, repr(user_id), fund_type)
                db.update_data_in_db(update_sql)
            else:
                update_sql = """UPDATE {3} 
                                SET availableBalance = {0}, frozenBalance = {1}  
                                WHERE userId = {2};""".format(available_balance, frozen_balance, repr(user_id), fund_type)
                db.update_data_in_db(update_sql)
    except  Exception as err:
        print(err)
    else:
        print("更新成功！")
        #fiat_fund_sql = """SELECT * 
        #                  FROM {4} 
        #                 WHERE userId = {0};""" .format(repr(user_id))
        #for i, j in db.fetch_data_from_db(fiat_fund_sql)[0][""]
    finally:
        db.close_db()

if __name__ == '__main__':
    """
    #for i in ['UserFiatFunds', 'UserCoin2CoinFunds']:
    #initUserFundAccount(fund_type=i, user_name='手机商家', currency='all', available_balance=6666, frozen_balance=0)
    #initUserFundAccount(fund_type='UserCoin2CoinFunds', user_name='手机商家', currency='all', available_balance=10000, frozen_balance=0)
    #initUserFundAccount(fund_type='UserCoin2CoinFunds', user_name='邮箱商家', currency='all', available_balance=10000, frozen_balance=0)
    """
    initUserFundAccount(fund_type='UserFiatFunds', user_nickname='手机商家', currency='NZ', available_balance=100000, frozen_balance=0)
    