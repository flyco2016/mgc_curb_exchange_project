from utils import mydb


def delCanceledOrdersInDB(user_nickname="手机商家", currency=None):
    """
    函数名：从数据库里面删除指定商家或者币种的已取消订单，不传币种则删除该用户所有已取消订单
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
            update_sql_1 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE userId = {0}
                              AND orderStatus = 6;""".format(repr(user_id))
            db.update_data_in_db(update_sql_1)

            update_sql_2 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE adUserId = {0}
                              AND orderStatus = 6;""".format(repr(user_id))
            db.update_data_in_db(update_sql_2)
        else:
            update_sql_3 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE userId = {0}
                              AND tradeCode = {1}
                              AND orderStatus = 6;""".format(repr(user_id), repr(currency))
            db.update_data_in_db(update_sql_3)

            update_sql_4 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE adUserId = {0}
                              AND tradeCode = {1}
                              AND orderStatus = 6;""".format(repr(user_id), repr(currency))
            db.update_data_in_db(update_sql_4)
    except Exception as err:
        print(err)
    else:
        print("删除已取消订单成功！")
    finally:
        db.close_db()

def delFinishedOrdersInDB(user_nickname="手机商家", currency=None):
    """
    函数名：从数据库里面删除指定商家或者币种的已完成订单，不传币种则删除该用户所有的已完成订单
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
            update_sql_1 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE userId = {0}
                              AND orderStatus = 3
                              AND tradeStatus = 2;""".format(repr(user_id))
            db.update_data_in_db(update_sql_1)

            update_sql_2 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE adUserId = {0}
                              AND orderStatus = 3
                              AND tradeStatus = 2;""".format(repr(user_id))
            db.update_data_in_db(update_sql_2)
        else:
            update_sql_3 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE userId = {0}
                              AND tradeCode = {1}
                              AND orderStatus = 3
                              AND tradeStatus = 2;""".format(repr(user_id), repr(currency))
            db.update_data_in_db(update_sql_3)

            update_sql_4 = """DELETE 
                              FROM FiatDealTradeOrder 
                              WHERE adUserId = {0}
                              AND tradeCode = {1}
                              AND orderStatus = 3
                              AND tradeStatus = 2;""".format(repr(user_id), repr(currency))
            db.update_data_in_db(update_sql_4)
    except Exception as err:
        print(err)
    else:
        print("删除已完成订单成功！")
    finally:
        db.close_db()

if __name__ == '__main__':
    delCanceledOrdersInDB(user_nickname='手机商家', currency='all')
    delFinishedOrdersInDB(user_nickname='手机商家', currency='all') 
