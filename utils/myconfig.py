import configparser
import sys
import os

class OverrideConf(configparser.ConfigParser):
    """
    重写optionxform方法，避免模块读取、写入文件时自动转换为小写字符的问题
    """
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)
    def optionxform(self, optionstr):
        return optionstr
    
class MyConfigParser():
    def __init__(self):
        """
        产生实例化
        """
        self.config = OverrideConf()
    
    def write_config(self, filename, section, key_list, value_list):
        """
        写入配置
        """
        if self.config.has_section(section):
            pass
        else:
            filename = filename + '.ini'
            self.config.add_section(section)  # 加入section
            for i in zip(key_list, value_list):   # 加入键值对
                self.config.set(section, i[0], i[1])
            with open(filename, 'a') as fp:
                self.config.write(fp)
    
    def add_section_in_config(self, filename, section):
        """
        增加section
        """
        try:
            filename = filename + '.ini'
            self.config.read(filename)
            self.config.add_section(section)
            with open(filename, 'a') as fp:
                self.config.write(fp)
        except configparser.DuplicateOptionError as err:
            print(err)
    
    def update_config(self, filename, section, **kwargs):
        """
        更新配置
        """
        filename = filename + '.ini'
        try:
            self.config.read(filename)
            if os.path.exists(filename):  # 判断文件存在，存在则更新
                if section not in self.config.sections():
                    print("update fail, section doesn't exists!")
                else:
                    for i ,j in kwargs.items():
                        self.config.set(section, i, j)
                    with open(filename, 'w') as fp:
                        self.config.write(fp)
                    print('update successfully!')
            else:   # 文件不存在提示
                print("file doesn't exists!")
        except configparser.NoSectionError as err:
            print(err)
        except TypeError as err:  # 捕捉TypeError异常
            print(err)
        except:
            print(sys.exc_info()[0])
    
    def delete_section(self, filename, section):
        """
        删除section
        """
        try:
            filename = filename + '.ini'
            self.config.read(filename)
            self.config.remove_section(section)
            with open(filename, 'a') as fp:
                self.config.write(fp)
        except configparser.NoSectionError as err:
            print(err)
    
    def delete_item(self, filename, section, key):
        """
        删除指定section中的item
        """
        try:
            filename = filename + '.ini'
            self.config.read(filename)
            self.config.remove_option(section, key)
            with open(filename, 'a') as fp:
                self.config.write(fp)
        except configparser.NoOptionError as err:
            print(err)
        except configparser.NoSectionError as err:
            print(err)

    def read_config(self, filename, section):
        """
        读取指定section的item
        """
        try:
            filename = filename + '.ini'
            self.config.read(filename)
            return self.config.items(section)
        except configparser.NoSectionError as err:
            print(err)
    
    def get_config_value(self, filename, section, key):
        """
        获取值
        """
        filename = "./config/" + filename + '.ini'
        self.config.read(filename, encoding='utf-8')
        return self.config.get(section, key)
        
if __name__ == '__main__':
    # 增加配置
    mycfg = MyConfigParser()
    filename = 'myini'
    section = 'mysql_221'
    key_list = ['host', 'port', 'user', 'password']
    value_list = ['192.168.22.221', '3306', 'mgcex', '123456']
    mycfg.write_config(filename, section, key_list, value_list)
    
    # 更新配置测试
    mycfg.update_config("myini", 'mysql', port='3300')   # 测试section错误的情况，pass
    mycfg.update_config("myini1", 'mysql_221', port='3300')   # 测试文件不存在，pass
    mycfg.update_config("myini", 'mysql_221', database_name='mgcex')   # 测试增加新的字段，pass
    mycfg.update_config("myini", 'mysql_221', database_name=123)   # 触发异常被捕捉，pass
    mycfg.update_config("myini", 'mysql_221', NOT_LOWER_STR="大写的")   # 测试防止小写读写，pass
    mycfg.add_section_in_config('myini', 'mysection')    
