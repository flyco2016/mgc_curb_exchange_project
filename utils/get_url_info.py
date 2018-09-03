from utils import myconfig

url_config = myconfig.MyConfigParser()


"""
用户中心url
"""
login_url = url_config.get_config_value("urlconfig", "user_center_url", 'login_url')
modifypwd_url = url_config.get_config_value("urlconfig", "user_center_url", 'modifypwd_url')
identity_url = url_config.get_config_value("urlconfig", "user_center_url", 'identity_url')
"""
获取用户资产url
"""
get_fiat_fund_account_url = url_config.get_config_value("urlconfig", "fund_account_url", 'get_fiat_fund_account_url')
get_coin_fund_account_url = url_config.get_config_value("urlconfig", "fund_account_url", 'get_coin_fund_account_url')

"""
法币交易url
"""
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
