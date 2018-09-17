from utils import myconfig

url_config = myconfig.MyConfigParser()


"""
用户中心url
"""
# 发送手机验证码
send_phone_authcode_url = url_config.get_config_value("urlconfig", "user_center_url", 'send_phone_authcode_url')
# 发送邮箱验证码
send_email_authcode_url = url_config.get_config_value("urlconfig", "user_center_url", 'send_email_authcode_url')
# 注册
register_url = url_config.get_config_value("urlconfig", "user_center_url", 'register_url')
# 登录
login_url = url_config.get_config_value("urlconfig", "user_center_url", 'login_url')
# 修改登录密码
modifypwd_url = url_config.get_config_value("urlconfig", "user_center_url", 'modifypwd_url')
# 身份认证
identity_url = url_config.get_config_value("urlconfig", "user_center_url", 'identity_url')
# 资金密码
money_password_url = url_config.get_config_value("urlconfig", "user_center_url", 'money_password_url')

"""
获取用户资产url
"""
# 获取法币账户
get_fiat_fund_account_url = url_config.get_config_value("urlconfig", "fund_account_url", 'get_fiat_fund_account_url')
# 获取币币账户
get_coin_fund_account_url = url_config.get_config_value("urlconfig", "fund_account_url", 'get_coin_fund_account_url')

"""
法币交易url
"""
# 申请商家
apply_for_merchant_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'apply_for_merchant_url')
# 发布广告
advertising_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'advertising_url')
# 取消广告
cancel_ad_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'cancel_ad_url')
# 获取广告列表
get_ad_list_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'get_ad_list_url')
# 获取国际行情
get_international_quotation_url = url_config.get_config_value("urlconfig", "international_url", 'get_international_quotation_url')
# 法币下单
place_fiat_order_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'place_fiat_order_url')
# 法币取消订单
cancel_order_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'cancel_order_url')
# 获取法币订单
get_fiat_order_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'get_fiat_order_url')
# 更新法币订单
update_fiat_order_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'update_fiat_order_url')
# 申诉
appeal_url = url_config.get_config_value("urlconfig", "curb_exchange_url", 'appeal_url')

"""
币币交易
"""
# 获取盘面行情
get_surface_quotation_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_surface_quotation_url')
# 委托下单
add_entrustment_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'add_entrustment_url')
# 获取当前委托
get_current_entrustments_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_current_entrustments_url')
# 获取历史委托
get_history_entrustments_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_history_entrustments_url')
# 获取最新的成交记录
get_c2c_deal_record_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_c2c_deal_record_url')
# 添加自选
add_collection_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'add_collection_url')
# 删除自选
del_collection_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'del_collection_url')
# 获取自选
get_collection_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_collection_url')
# 获取币种的最小交易量
get_minimum_transaction_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_minimum_transaction_url')
# 获取买卖五档
get_buy_and_sell_five_gears_url = url_config.get_config_value("urlconfig", "Coin2Coin_exchange_url", 'get_buy_and_sell_five_gears_url')