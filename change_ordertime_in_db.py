from utils import mydb
import time

def ChangeOrderTimeInDB(order_ID_NO=None, delta_time=20):
    """
    函数名：ChangeOrderTimeInDB
    函数功能：从数据库里面订单下单修改时间，时间格式为2018-09-05 11:35:06
    输入参数：订单号order_ID_NO, delta_time为时间变量，单位是min，负数则将时间回拨，正数则将时间前挪
    输出参数：None
    """
    try:
        db = mydb.MyDB()
        get_ordertime_sql = """SELECT * 
                               FROM FiatDealTradeOrder 
                               WHERE tradeOrderId = {};""".format(order_ID_NO)
        order_time = db.fetch_data_from_db(get_ordertime_sql)[0]["orderTime"]
        print("订单更新前的时间为:{}".format(order_time))
        # 转为时间数组
        time_array = time.strptime(str(order_time), "%Y-%m-%d %H:%M:%S")
        # 转换为时间戳
        old_timestamp = int(time.mktime(time_array))
        new_timestamp = old_timestamp + delta_time * 60
        # 将新的时间戳转换为格式化的时间
        new_order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(new_timestamp))
        #print(new_order_time, type(new_order_time))
        change_order_time_sql = """UPDATE FiatDealTradeOrder 
                                   SET orderTime = {0} 
                                   WHERE tradeOrderId = {1};""".format(repr(new_order_time), order_ID_NO)
        db.update_data_in_db(change_order_time_sql)
    except Exception as err:
        print(err)
    else:
        print("更新下单时间成功,更新后的时间为:{}".format(new_order_time))
    finally:
        db.close_db()

if __name__ == '__main__':
    for i in range(4):
        ChangeOrderTimeInDB(order_ID_NO='1536132964574021461', delta_time=-20) 
