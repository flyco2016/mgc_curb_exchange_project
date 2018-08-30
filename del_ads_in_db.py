from utils import mydb


def delOrdersInDB(user_nickname="手机商家", currency=None):
    """
    函数名：从数据库里面删除指定商家或者币种的广告单，不传币种则删除该用户所用的广告单，这些广告单是解冻的广告单
    函数功能：
    输入参数：
    输出参数：
    """
    try:
        db = mydb.MyDB()

        user_sql = """SELECT * 
                      FROM User 
                      WHERE nikeName = {0};""".format(repr(user_nickname))
        user_id = db.fetch_data_from_db(user_sql)[0]["userId"]
        if (currency == 'all'):
            update_sql = """DELETE 
                            FROM Advertising 
                            WHERE userId = {0}
                            AND frozenStatus = 1
                            AND frozenOrderVal = 0;""".format(repr(user_id))
            db.update_data_in_db(update_sql)
        else:
            update_sql = """DELETE 
                            FROM Advertising 
                            WHERE userId = {0}
                            AND tradeCode = {1}
                            AND frozenStatus = 1
                            AND frozenOrderVal = 0;""".format(repr(user_id), repr(currency))
            db.update_data_in_db(update_sql)
    except Exception as err:
        print(err)
    else:
        print("删除成功！")
        #fiat_fund_sql = """SELECT * 
        #                  FROM {4} 
        #                 WHERE userId = {0};""" .format(repr(user_id))
        #for i, j in db.fetch_data_from_db(fiat_fund_sql)[0][""]
    finally:
        db.close_db()

if __name__ == '__main__':
    delOrdersInDB(user_nickname='手机商家', currency='all') 
