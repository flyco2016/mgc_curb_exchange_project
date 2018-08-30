from utils import myconfig

jsonstring_config = myconfig.MyConfigParser()

"""
用户中心jsonstring
"""
login_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'login_jsonString')
modifypwd_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'modifypwd_jsonString')
identity_IDcard_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'identity_IDcard_jsonString')
identity_passport_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'identity_passport_jsonString')

"""
获取资金账户
"""
get_fiat_fund_account_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "fund_account_jsonString", 'get_fiat_fund_account_jsonString')
get_coin_fund_account_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "fund_account_jsonString", 'get_coin_fund_account_jsonString')


"""
法币交易jsonstring
"""
# 发布广告
limited_price_buy_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'limited_price_buy_ad_jsonString')
market_price_buy_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'market_price_buy_ad_jsonString')
limited_price_sell_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'limited_price_sell_ad_jsonString')
market_price_sell_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'market_price_sell_ad_jsonString')

# 撤销广告单
cancel_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'cancel_ad_jsonString')

# 获取广告单
get_buy_ad_list_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'get_buy_ad_list_jsonString')
get_sell_ad_list_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'get_sell_ad_list_jsonString')

# 法币下单
buy_fiat_order_limited_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buy_fiat_order_limited_jsonString")
buy_fiat_order_market_by_quantity_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buy_fiat_order_market_by_quantity_jsonString")
buy_fiat_order_market_by_amount_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buy_fiat_order_market_by_amount_jsonString")
sell_fiat_order_limited_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "sell_fiat_order_limited_jsonString")
sell_fiat_order_market_by_quantity_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "sell_fiat_order_market_by_quantity_jsonString")
sell_fiat_order_market_by_amount_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "sell_fiat_order_market_by_amount_jsonString")

# 取消法币订单
cancel_order_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "cancel_order_jsonString")

# 获取国际行情
get_international_quotation_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "international_quotation_jsonString", 'get_international_quotation_jsonString')
