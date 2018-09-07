from utils import mydb


def delUserRegInfoInDB(sql):
    """
    函数名：getUserInfoInDB
    函数功能：在数据库中获取某个用户的各种信息
    输入参数
    """
    try:
        db = mydb.MyDB()
        for i in sql:
            db.update_data_in_db(i) 
    except Exception as err:
        print(err)
    else:
        pass
    finally:
        db.close_db()

def quickToDel():
    sql_1 = "DELETE FROM `User` WHERE nikeName LIKE '1772781000%';"
    sql_2 = "DELETE FROM UserEmail WHERE email LIKE '1772781000%@163.com';"
    sql_3 = "DELETE FROM UserTelphone WHERE telphone BETWEEN '17727810000' AND '17727810004';"
    sql_tuple = sql_1, sql_2, sql_3
    #print(sql_tuple)
    delUserRegInfoInDB(sql_tuple)
    print('删除原来注册的账户成功')

if __name__ == '__main__':
    quickToDel()


    
