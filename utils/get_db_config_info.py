from utils import myconfig

db_config = myconfig.MyConfigParser()

"""
数据库url
"""
dbname = db_config.get_config_value("dbconfig", "mysql_221", 'dbname')
dbhost = db_config.get_config_value("dbconfig", "mysql_221", 'dbhost')
dbuser = db_config.get_config_value("dbconfig", "mysql_221", 'dbuser')
dbpassword = db_config.get_config_value("dbconfig", "mysql_221", 'dbpassword')
dbport = db_config.get_config_value("dbconfig", "mysql_221", 'dbport')