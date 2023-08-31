import os
from crawler.data_deal import data_deal
# from crawler.login import loin
from crawler.mysql_init import data_to_mysql
from crawler.spider import wuyou
import configparser
import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    url = 'https://login.51job.com/login.php?loginway=0&isjump=0&lang=c&from_domain=i&url=http%3A%2F%2Fwww.51job.com%2F'
    cfp = configparser.RawConfigParser()
    cfp.read('config.ini', encoding='utf-8')
    crawler_list = cfp.get('crawler', 'list_data')
    try:
        os.remove('static/data.csv')
    except:
        pass
    list_data = crawler_list.split(',')  # 获取需求关键词
    # loin(url)  # 登录
    wy = wuyou()  # 实例化
    print('数据爬取中！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
    print('------*********--------------------信息展示--------------------*********------')
    for i in list_data:
        wy.data_tocsv(i, 10)  # 这里这个写爬多少页目前是40页
    print('爬取完毕！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
    print("开始数据清洗！")
    data_deal()
    print("正在数据保存到mysql！")
    data_to_mysql()
