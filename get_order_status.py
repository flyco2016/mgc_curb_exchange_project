import requests
import time
from login import login
from utils import get_url_info
from utils import get_jsonstring_info

def getOrderStatus(user_name='17727820013', password='123456', order_ID_NO=None):
    """
    函数功能：获取指定法币订单的状态
    函数输入说明：
    user_name---用户昵称
    password---登录密码
    order_ID_NO---订单号
    函数返回说明：
    返回一个字典类型，每个键值解析如下
    trade_volume---交易总量，单位为币种的数量
    currency---该订单的币种
    pay_identification_code---付款标识码
    trade_amount---交易总额，数量乘以单价
    unit_price---单价，人民币
    order_time---下单时间
    appeal_status---该订单的申诉状态，1为未申诉，2为申诉中，3为申诉已判定
    order_status---订单状态，1未付款，2已付款，3已收款，4已发货，5已超时，6已取消
    """
    try:
        mytoken = login(login_num=user_name, password=password)["data"]["token"]
        jsonString = get_jsonstring_info.get_fiat_order_jsonString %(repr(order_ID_NO))        
        data = dict(jsonString=jsonString)
        headers = {"token": mytoken}
        r = requests.post(get_url_info.get_fiat_order_url, data=data, headers=headers)
        if r.json()['msg'] == '操作完成':
            temp_dict = r.json()['data']
            result_dict = dict(trade_volume=temp_dict['tradeQuantity'], 
                            currency=temp_dict['tradeCode'],
                            pay_identification_code=temp_dict['payIdentificationCode'],
                            trade_amount=temp_dict['tradeAmount'],
                            unit_price=temp_dict['priceVal'],
                            order_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(temp_dict['orderTime'])/1000)),  # 转换为时间戳，注意原来的接口返回的是毫秒 
                            appeal_status=temp_dict['appealStatus'],
                            order_status=temp_dict['orderStatus']
                            )
            return result_dict
        else:
            print(r.json()['msg'])
        
    except Exception as err:
        print(err)


if __name__ == '__main__':
    r = getOrderStatus(order_ID_NO='1535979259612489838')
    print(r)
    print(r['order_time'])



        
