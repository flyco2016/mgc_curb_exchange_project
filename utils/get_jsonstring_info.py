from utils import myconfig

jsonstring_config = myconfig.MyConfigParser()

"""
用户中心jsonstring
"""
# 发送手机验证码
send_phone_authcode_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'send_phone_authcode_jsonString')
# 发送邮箱验证码
send_email_authcode_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'send_email_authcode_jsonString')
# 通过PC注册账号
register_through_PC_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'register_through_PC_jsonString')
# 通过安卓注册账号
register_through_Android_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'register_through_Android_jsonString')
# 通过IOS注册账号
register_through_IOS_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'register_through_IOS_jsonString')
# 通过H5注册账号（带邀请码）
register_through_H5_with_inviterCode_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'register_through_H5_with_inviterCode_jsonString')
# 通过H5注册账号（不带邀请码）
register_through_H5_without_inviterCode_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'register_through_H5_without_inviterCode_jsonString')
# 登录
login_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'login_jsonString')
# 修改密码
modifypwd_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'modifypwd_jsonString')
# 通过身份证认证
identity_IDcard_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'identity_IDcard_jsonString')
# 通过护照认证
identity_passport_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "user_center_jsonString", 'identity_passport_jsonString')

"""
获取资金账户
"""
# 获取法币账户
get_fiat_fund_account_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "fund_account_jsonString", 'get_fiat_fund_account_jsonString')
# 获取币币账户
get_coin_fund_account_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "fund_account_jsonString", 'get_coin_fund_account_jsonString')

"""
法币交易jsonstring
"""
# 发布限价求购广告
limited_price_buy_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'limited_price_buy_ad_jsonString')
# 发布市价求购广告
market_price_buy_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'market_price_buy_ad_jsonString')
# 发布限价卖出广告
limited_price_sell_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'limited_price_sell_ad_jsonString')
# 发布市价卖出广告
market_price_sell_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'market_price_sell_ad_jsonString')
# 撤销广告单
cancel_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'cancel_ad_jsonString')
# 获取求购广告单列表
get_buy_ad_list_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'get_buy_ad_list_jsonString')
# 获取卖出广告单列表
get_sell_ad_list_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'get_sell_ad_list_jsonString')
# 获取单个广告单
get_single_ad_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", 'get_single_ad_jsonString')
# 法币下单---限价买入
buy_fiat_order_limited_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buy_fiat_order_limited_jsonString")
# 法币下单---市价按数量买入
buy_fiat_order_market_by_quantity_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buy_fiat_order_market_by_quantity_jsonString")
# 法币下单---市价按总额买入
buy_fiat_order_market_by_amount_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buy_fiat_order_market_by_amount_jsonString")
# 法币下单---限价卖出
sell_fiat_order_limited_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "sell_fiat_order_limited_jsonString")
# 法币下单---市价按数量卖出
sell_fiat_order_market_by_quantity_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "sell_fiat_order_market_by_quantity_jsonString")
# 法币下单---市价按总额卖出
sell_fiat_order_market_by_amount_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "sell_fiat_order_market_by_amount_jsonString")
# 取消法币订单
cancel_order_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "cancel_order_jsonString")
# 获取单个法币订单
get_fiat_order_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "get_fiat_order_jsonString")
# 更新法币订单状态
update_fiat_order_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "update_fiat_order_jsonString")
# 卖方申诉---银行卡
seller_appeal_through_bank_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "seller_appeal_through_bank_jsonString")
# 卖方申诉---支付宝
seller_appeal_through_Alipay_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "seller_appeal_through_Alipay_jsonString")
# 卖方申诉---微信
seller_appeal_through_Wechat_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "seller_appeal_through_Wechat_jsonString")
# 买方申诉---银行卡
buyer_appeal_through_bank_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buyer_appeal_through_bank_jsonString")
# 买方申诉---支付宝
buyer_appeal_through_Alipay_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buyer_appeal_through_Alipay_jsonString")
# 买方申诉---微信
buyer_appeal_through_Wechat_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "curb_exchange_jsonString", "buyer_appeal_through_Wechat_jsonString")

"""
行情相关的法币交易jsonstring
"""
# 获取国际行情
get_international_quotation_jsonString = jsonstring_config.get_config_value("jsonStringconfig", "international_quotation_jsonString", 'get_international_quotation_jsonString')
