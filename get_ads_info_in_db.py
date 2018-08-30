from utils import mydb
import advertising

def getAdInfo(ad_ID_NO=None):
    try:
        db = mydb.MyDB()
        # 多行注释先ctrl+c，ctrl+k
        # user_sql = """SELECT * 
        #               FROM User 
        #               WHERE nikeName = {0};""".format(repr(user_nickname))
        # user_id = db.fetch_data_from_db(user_sql)[0]["userId"]

        sql = """SELECT * 
                 FROM Advertising 
                 WHERE advertisingOrderId = {0}
                 ;""".format(repr(ad_ID_NO))
        r = db.fetch_data_from_db(sql)
        return r
    except Exception as err:
        print(err)

def getAdIDByUser(user_nickname=None, currency=None):
    try:
        db = mydb.MyDB()
        # 多行注释先ctrl+c，ctrl+k
        # user_sql = """SELECT * 
        #               FROM User 
        #               WHERE nikeName = {0};""".format(repr(user_nickname))
        # user_id = db.fetch_data_from_db(user_sql)[0]["userId"]

        sql = """SELECT * 
                 FROM Advertising 
                 WHERE nickname = {0}
                 AND tradeCode = {1}
                 ;""".format(repr(user_nickname), repr(currency))
        r = db.fetch_data_from_db(sql)
        return [i['advertisingOrderId'] for i in r]
    except Exception as err:
        print(err)

def getUserInfoByAdID(ad_ID_NO=None):
    try:
        db = mydb.MyDB()
        # 多行注释先ctrl+c，ctrl+k
        # user_sql = """SELECT * 
        #               FROM User 
        #               WHERE nikeName = {0};""".format(repr(user_nickname))
        # user_id = db.fetch_data_from_db(user_sql)[0]["userId"]

        sql = """SELECT * 
                 FROM Advertising 
                 WHERE AdvertisingOrderId = {0};""".format(repr(ad_ID_NO))
        r = db.fetch_data_from_db(sql)
        return [i['userId'] for i in r]
    except Exception as err:
        print(err)
    
def judgeIfLimitedPrice(ad_ID_NO=None):
    if getAdInfo(ad_ID_NO=ad_ID_NO)[0]['type'] == 2:
        return True
    else:
        return False

def judgeIfMarketdPrice(ad_ID_NO=None):
    if getAdInfo(ad_ID_NO=ad_ID_NO)[0]['type'] == 1:
        return True
    else:
        return False        
    
    
    


if __name__ == "__main__":
    """
    advertising.limitedPriceBuyAd(currency='NZ', price=1, 
    amount=1000, floor=1, ceiling=1000)
    
    for i in getAdIDByUser(user_nickname='手机商家', currency='NZ'):
        for j in getUserInfoByAdID(ad_ID_NO=i):
            print(j)
    
    print(judgeIfLimitedPrice(ad_ID_NO='fa1535333912152284728'))
    """

    advertiser_userid = getAdInfo(ad_ID_NO='fa1535333912152284728')[0]['userId']
        
    currency = getAdInfo(ad_ID_NO='fa1535333912152284728')[0]['tradeCode']

    unit_price = getAdInfo(ad_ID_NO='fa1535333912152284728')[0]['priceVal']

    print(advertiser_userid, currency, unit_price, sep='\n')
    
    print(type(getAdInfo(ad_ID_NO='fa1535333912152284728')[0]['buysell']))



    
        
    
