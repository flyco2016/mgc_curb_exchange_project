from utils import mydb

def getEntrustmentIdInDB(entrustment_ID_NO=None):
    try:
        db = mydb.MyDB()
        # 多行注释先ctrl+c，ctrl+k
        # user_sql = """SELECT * 
        #               FROM User 
        #               WHERE nikeName = {0};""".format(repr(user_nickname))
        # user_id = db.fetch_data_from_db(user_sql)[0]["userId"]

        sql = """SELECT * 
                 FROM Entrustment 
                 WHERE id = {0}
                 ;""".format(repr(entrustment_ID_NO))
        r = db.fetch_data_from_db(sql)
        return r[0]['id']
    except Exception as err:
        print(err)
    finally:
        db.close_db()

if __name__ == '__main__':
    print(getEntrustmentIdInDB(entrustment_ID_NO="000CC5975087AAC0D5120429095BF8B8"))
