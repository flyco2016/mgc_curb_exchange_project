import requests
from login import login
from utils import get_url_info
from utils import get_jsonstring_info

def getInternationalQuotation(currency=None):
    try:
        jsonString = get_jsonstring_info.get_international_quotation_jsonString % (repr(currency))
        data = dict(jsonString=jsonString)

        r = requests.post(get_url_info.get_international_quotation_url, data=data)
        return r.json()['data'][0]['price']
    except Exception as err:
        print(err)
    
if __name__ == "__main__":
    r = getInternationalQuotation(currency='NZ')
    print(r)
