from utils import mydb


def delDoneCompletelyEnstrustmentsInDB(user_name=None, market=None, symbol=None):
    """
    函数功能：从数据库里面删除完全成交的委托单，如果不传任何参数，则默认删除自己用户的所有交易对的数据
    输入参数：
    输出参数：
    """
    try:
        db = mydb.MyDB()
                
        if (user_name==None) and (market==None) and (symbol==None):
            # 不传任何参数时删除所有完全成交的委托单
            update_sql = """DELETE 
                            FROM Entrustment 
                            WHERE userId = 
                            (SELECT userId 
                             FROM UserTelphone 
                             WHERE telphone = {0}
                            )
                            'status' = 3;""".format(repr(user_name))
            db.update_data_in_db(update_sql)
        elif user_name != None:
            update_sql = """DELETE 
                            FROM Entrustment 
                            WHERE userId = 
                            (SELECT userId 
                             FROM UserTelphone 
                             WHERE telphone = {0}
                            )
                            AND 'status' = 3
                            AND market = {1}
                            AND symbol = {2};""".format(repr(user_name), repr(market), repr(symbol))            
            db.update_data_in_db(update_sql)
    except Exception as err:
        print(err)
    finally:
        db.close_db()

def delCanceledEnstrustmentsInDB(user_name=None, market=None, symbol=None):
    """
    函数功能：从数据库里面删除已经删除的委托单，如果不传user_name
    输入参数：
    输出参数：
    """
    try:
        db = mydb.MyDB()
                
        if (user_name==None) and (market==None) and (symbol==None):
            # 不传任何参数时删除所有完全成交的委托单
            update_sql = """DELETE 
                            FROM Entrustment 
                            WHERE 'status' = 5;"""
            db.update_data_in_db(update_sql)
        elif user_name != None:
            update_sql = """DELETE 
                            FROM Entrustment 
                            WHERE userId = 
                            (SELECT userId 
                             FROM UserTelphone 
                             WHERE telphone = {0}
                            )
                            AND 'status' = 5
                            AND market = {1}
                            AND symbol = {2};""".format(repr(user_name), repr(market), repr(symbol))            
            db.update_data_in_db(update_sql)
    except Exception as err:
        print(err)
    finally:
        db.close_db()



if __name__ == '__main__':
    delDoneCompletelyEnstrustmentsInDB(user_name='17727820013')
    delCanceledEnstrustmentsInDB(user_name='17727820013')
