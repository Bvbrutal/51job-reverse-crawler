import pandas as pd
from flask import Flask, render_template
import pymysql
from crawler.get_information import get_information, get_setting

mysql_password,mysql_root,host_ip=get_information()

app = Flask(__name__)
from sqlalchemy import create_engine

@app.before_first_request
def load_data():
    global data_all
    global data_show
    sql_cmd_all = "SELECT * FROM jobdata"
    sql_cmd_show = "SELECT * FROM jobdata LIMIT 100"
    # 创建Engine连接MySQL数据库
    # url = f"mysql+mysqldb://{mysql_root}:{mysql_password}@{host_ip}:3306/sqlalchemy?charset=utf8"
    # engine = create_engine(url=url, echo=True, future=True)

    engine = pymysql.connect(host=host_ip, user=mysql_root, password=mysql_password, database='51job', charset='utf8',
                          use_unicode=True)

    data_all = pd.read_sql(sql_cmd_all, engine)
    data_show = pd.read_sql(sql_cmd_show, engine)
    engine.close()



def get_data():
    return data_all
def get_data_show():
    return data_show
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/pythoninfo')
def pythoninfo():
    df=get_data_show()
    return render_template('pythoninfo.html',data=df)


@app.route('/analysis')
def analysis():
    #data1
    df = get_data()
    df1=df['地区'].value_counts()
    #data2
    df2=df[['学历要求','招收对象']].value_counts()
    # data3
    df3=df['企业类别'].value_counts()
    #data4
    df4 = df['薪资'].value_counts()
    xdata = []
    ydata = []
    for i in sorted(df4.items(), key=lambda x: int(x[0])):
        xdata.append(i[0])
        ydata.append(i[1])
    #data5
    df5 = df[['薪资']].value_counts().apply(lambda x :x/df.shape[0])
    df6=df['企业类别'].value_counts().apply(lambda x: x / df.shape[0])
    df7=df[['学历要求','招收对象']].value_counts().apply(lambda x: x / df.shape[0])
    return render_template('analysis.html', df1=df1,df2=df2 ,df3=df3,xdata=xdata,ydata=ydata,df4=df4,df5=df5,df6=df6,df7=df7)


@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')


@app.route('/test')
def show():
    df = get_data()
    df1=df['地区'].value_counts()
    df2=df['岗位名称'].value_counts()
    df3=df[['公司全称','更新时间']].drop_duplicates(keep='first').groupby('更新时间').count()['公司全称']
    df4=df[['岗位名称','更新时间']].groupby('更新时间').count()['岗位名称']
    return render_template('show.html',df=df,df1=df1,df2=df2,df3=df3,df4=df4)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
