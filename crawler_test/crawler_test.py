# -*- coding: UTF-8 -*-
import configparser


# cfp = configparser.RawConfigParser()
# cfp.read('config.ini',encoding='utf-8')
#
# crawler_list=cfp.get('crawler', 'list_data')
#
# crawler_list.split(',')
#
# print(type(crawler_list.split(',')))


cfp = configparser.RawConfigParser()
cfp.read('config.ini', encoding='utf-8')
phonenumber = cfp.get('personal', 'phonenumber')
password=cfp.get('personal', 'password')
print(phonenumber,password)