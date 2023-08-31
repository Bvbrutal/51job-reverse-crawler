import pymysql
import pandas as pd

from crawler.get_information import get_information, get_setting

mysql_password,mysql_root=get_information()
reget_data=get_setting()


def mysql_init(sql):
    db = pymysql.connect(host='127.0.0.1',
                         user=mysql_root,
                         password=mysql_password,
                         database='51job')
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.close()  # 关闭当前游标
    db.close()


def mysql_db_init():
    db = pymysql.connect(host='127.0.0.1',
                         user=mysql_root,
                         password=mysql_password)
    # 指定要创建的数据库名
    db_name = '51job'
    # 创建一个游标对象
    cursor = db.cursor()
    # 使用 SQL 查询语句创建数据库
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
    cursor.execute(create_db_query)
    # 关闭游标
    cursor.close()



def data_to_mysql():
    sql1 = '''create table IF NOT EXISTS jobdata (公司全称 varchar(255),岗位名称 varchar(255),地区 varchar(255),薪资 varchar(255),学历要求 varchar(255),职业类别 varchar(255),招收对象 varchar(255),企业类别 varchar(255),关键字 varchar(255),更新时间 varchar(255))'''
    mysql_db_init()
    # sql2 = '''DROP TABLE IF EXISTS jobdata;'''
    # mysql_init(sql2)
    mysql_init(sql1)
    df=pd.read_csv('static/data.csv', header=None)
    db = pymysql.connect(host='127.0.0.1',
                         user=mysql_root,
                         password=mysql_password,
                         database='51job')
    cursor = db.cursor()
    if reget_data:
        sql_del = '''delete from jobdata'''
        cursor.execute(sql_del)
        db.commit()
    for i in range(df.shape[0]):
        sql = "insert into jobdata (公司全称,岗位名称,地区,薪资,学历要求,职业类别,招收对象,企业类别,关键字,更新时间) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        cursor.execute(sql%(df[0][i],df[1][i],df[5][i],df[6][i],df[2][i],df[11][i],df[8][i],df[3][i],df[7][i].replace("'",''),df[10][i]))
    db.commit()
    cursor.close()  # 关闭当前游标
    db.close() #关闭数据库
    print('数据已经存入数据库！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')

if __name__ == '__main__':
    data_to_mysql()