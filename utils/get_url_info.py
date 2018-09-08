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