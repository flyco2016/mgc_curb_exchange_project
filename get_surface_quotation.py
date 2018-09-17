import requests
import json
from utils import get_url_info


def getSurfaceQuotation(symbol='BTC', market='NZ'):
    """
    函数功能：获取盘面交易对的行情
    输入参数：
    market---市场（作为主链）
    symbol---币种（子链，是买卖的币种）
    输出参数：
    字典类型，详细的键值对说明如下
    date---日期
    yesterday_closing_price---昨日收盘价
    open_price---开盘价
    top_price---最高价
    bottom_price---最低价
    closing_price---收盘价
    percentage_gain---涨幅
    newest_price---最新价
    newest_volume---最新成交量
    sell_price---卖价
    buy_price--买价
    valuation---估值
    acc_volume_24h---24H累积交易量
    acc_amount_24h---24H累积交易额
    acc_gains_24h---24H累积涨幅
    market_price---market的市场价格
    """
    payload = {"data": [{"tradeCode":"{market}:{symbol}".format(market=market, symbol=symbol)}]}
    r = requests.post(get_url_info.get_surface_quotation_url, data=json.dumps(payload))
    if r.json()['msg'] == '成功':
        import time
        temp = r.json()['data'][0]
        rdict = {}
        rdict.update(
                    date=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(temp['date'])),
                    yesterday_closing_price=temp['refClose'],
                    open_price=temp['o'],
                    closing_price=temp['c'],
                    top_price=temp['h'],
                    bottom_price=temp['l'],
                    percentage_gain=temp['gains'],
                    newest_price=temp['newPrice'],
                    newest_volume=temp['newVolume'],
                    sell_price=temp['sellPrice'],
                    buy_price=temp['buyPrice'],
                    valuation=temp['valuation'],
                    acc_volume_24h=temp['accVolume'],
                    acc_amount_24h=temp['accAmount'],
                    acc_gains_24h=temp['accGains'],
                    market_price=temp['marketPrice']
                    )
        return rdict
    else:
        print(r.json()['msg'])

if __name__ == '__main__':
    """
    symbol_list = ['ETH', 'EOS', 'LTC', 'USDT', 'BTC', 'OWN', 'KBC', 'HED', 'LTW']
    for symbol in symbol_list:
        r = getSurfaceQuotation(symbol=symbol, market='NZ')
        for k, v in r.items():
            print(k, '==>', v)
        print('\n')
    """
    print(getSurfaceQuotation(symbol='BTC', market='NZ'))

    