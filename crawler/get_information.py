import configparser
def get_information():
    cfp = configparser.RawConfigParser()
    cfp.read('config.ini', encoding='utf-8')
    mysql_password=cfp.get('mysql', 'mysql_password')
    mysql_root=cfp.get('mysql', 'mysql_root')
    return mysql_password,mysql_root


def get_setting():
    cfp = configparser.RawConfigParser()
    cfp.read('config.ini', encoding='utf-8')
    reget_data = bool(int(cfp.get('setting', 'reget_data')))
    return reget_data