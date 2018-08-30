import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info
import get_international_quotation

try:
    mytoken = login(loginNum=user_name, password=password)["data"]["token"]
    jsonString = get_jsonstring_info.limited_price_buy_ad_jsonString %(repr(currency), payment, price, 
    amount, floor, ceiling)        
    data = dict(jsonString=jsonString)
    headers = {"token": str(mytoken)}
    r = requests.post(get_url_info.advertising_url, data=data, headers=headers)
except Exception as err:
        print(err)

