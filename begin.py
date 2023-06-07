import os
from spider.data_deal import data_deal
from spider.login import loin
from spider.mysql_init import data_to_mysql
from spider.spider import wuyou

import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    try:
        os.remove('static/data.csv')
    except:
        pass
    list_data = ['python', 'java', '销售', '自动化', '软件', '通信', '车辆']  # 这里可以写要爬的关键词
    # loin()  # 登录
    wy = wuyou()  # 实例化
    print('数据爬取中！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
    print('------*********--------------------信息展示--------------------*********------')
    for i in list_data:
        wy.data_tocsv(i, 40)  # 这里这个写爬多少页目前是40页
    print('爬取完毕！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
    data_deal()
    data_to_mysql()