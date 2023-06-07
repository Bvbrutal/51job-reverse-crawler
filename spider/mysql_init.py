import pymysql
import pandas as pd

def mysql_init(sql):
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='123456',
                         database='51job')
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.close()  # 关闭当前游标
    db.close()

def data_to_mysql():
    sql1 = '''create table jobdata (公司全称 varchar(255),岗位名称 varchar(255),地区 varchar(255),薪资 varchar(255),学历要求 varchar(255),职业类别 varchar(255),招收对象 varchar(255),企业类别 varchar(255),关键字 varchar(255),更新时间 varchar(255))'''
    sql2= '''drop table jobdata'''
    try:
        mysql_init(sql2)
    except:
        pass
    try:
        mysql_init(sql1)
    except:
        pass
    df=pd.read_csv('static/data.csv', header=None)
    db = pymysql.connect(host='127.0.0.1',
                         user='root',
                         password='123456',
                         database='51job')
    sql_del = '''delete from jobdata'''
    cursor = db.cursor()
    cursor.execute(sql_del)
    db.commit()
    for i in range(df.shape[0]):
        sql = "insert into jobdata (公司全称,岗位名称,地区,薪资,学历要求,职业类别,招收对象,企业类别,关键字,更新时间) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        cursor.execute(sql%(df[0][i],df[1][i],df[5][i],df[6][i],df[2][i],df[11][i],df[8][i],df[3][i],df[7][i].replace("'",''),df[10][i]))
    cursor.close()  # 关闭当前游标
    db.commit()
    db.close()
    print('数据已经存入数据库！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')

if __name__ == '__main__':
    data_to_mysql()