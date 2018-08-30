import pymysql
import pymysql.cursors
from utils import myconfig
import sys

"""
# 写配置，形成配置文件,一般一次就够了
filename = "dbconfig"
section = 'mysql_221'
key_list = ['dbname', 'dbhost', 'dbuser', 'dbpassword', 'dbport']
value_list = ['mgcex', '172.16.11.221', 'mgcex', '123456', '3306']
config = myconfig.MyConfigParser()
config.write_config(filename, section, key_list, value_list)
"""


# 数据集
filename = "dbconfig"
section = 'mysql_221'
key_list = ['dbname', 'dbhost', 'dbuser', 'dbpassword', 'dbport']
value_list = ['mgcex', '192.168.13.221', 'mgcex', '123456', '3306']
config = myconfig.MyConfigParser()


# 读配置，生成连接必备的数据信息
DBNAME = config.get_config_value(filename, section, 'dbname')
DBHOST = config.get_config_value(filename, section, 'dbhost')
DBUSER = config.get_config_value(filename, section, 'dbuser')
DBPWD = config.get_config_value(filename, section, 'dbpassword')
DBPORT = int(config.get_config_value(filename, section, 'dbport'))

class MyDB:
    """
    自定义数据库类
    """
    def __init__(self, dbname=None, dbhost=None):
        if dbname is None:
            self._dbname = DBNAME
        else:
            self._dbname = dbname
        if dbhost is None:
            self._dbhost = DBHOST
        else:
            self._dbhost = dbhost
        self._dbuser = DBUSER
        self._dbpassword = DBPWD
        self._dbport = DBPORT
        self._conn = self.connMySQL()
        if self._conn:
            self._cursor = self._conn.cursor()
    
    def connMySQL(self):
        """
        连接数据库
        """
        conn = False
        try:
            conn = pymysql.connect(
                host=self._dbhost,
                user=self._dbuser,
                passwd=self._dbpassword,
                db=self._dbname,
                port=self._dbport,
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as err:
            print(err)
            conn = False
        return conn
    
    def fetch_data_from_db(self, sql):
        """
        查询数据库
        """
        res = ''
        if self._conn:
            try:
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as err:
                res = False
                print("query database exception, %s" % err)
        return res
    
    def update_data_in_db(self, sql):
        """
        更新数据库
        """
        flag = False
        if self._conn:
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception as err:
                flag = False
                print("updata database exception, {}".format(err))
        return flag
    
    def close_db(self):
        if self._conn:
            try:
                if (type(self._cursor)=='object'):
                    self._cursor.close()
                if (type(self._conn)=='object'):
                    self._conn.close()
            except Exception as err:
                print("close database exception,\
                 %s,%s,%s" % (err, type(self._cursor), \
                 type(self._conn)))

if __name__ == "__main__":
    telephone = '15013602610'
    sql_user = "SELECT * FROM `User` u INNER JOIN UserTelphone ut ON u.userId = ut.userId WHERE \
ut.telphone = {};".format(telephone)
    mydb = MyDB()   # 实例化221的数据库，使用默认的连接信息，顺便连接数据库
    print('开始进行{}用户的查询'.format(telephone))
    r = mydb.fetch_data_from_db(sql_user)   # 返回一个列表，列表里面是字典
    userId = r[0]['userId']
    nikeName = r[0]['nikeName']
    isVerifyIdentity = r[0]['isVerifyIdentity']
    isSetAcc = r[0]['isSetAcc']
    myInviteCode = r[0]['myInviteCode']

    print("获取到该用户的用户ID:{}".format(userId))

    if nikeName == '手机商家':
        print("该用户是商家")

    if isVerifyIdentity == 'Y':
        print("该用户已经通过了身份认证")
    elif isVerifyIdentity == 'N':
        print("该用户没有通过了身份认证")

    if isSetAcc == 'Y':
        print("该用户已经进行资金密码设置")
    elif isSetAcc == 'N':
        print("该用户没有进行资金密码设置")
    
    print("该用户的邀请码是{}".format(myInviteCode))
    
    mydb.close_db()   # 关闭数据库
    print("数据库关闭成功")
