import pandas as pd
import re
from datetime import datetime

def data_deal():
    global x, y
    df = pd.read_csv('static/data_undeal.csv', header=None, encoding='utf-8-sig')
    temp = pd.to_datetime(df[10])
    df[10] = temp.apply(lambda x: datetime.strftime(x, "%Y-%m-%d"))
    df = df.replace('[(（].*[）)]', '', regex=True)
    df.drop_duplicates(keep='first', inplace=True)  # 删除重复值
    df.reset_index(drop=True, inplace=True)
    for i in range(0, df.shape[0]):  # 0-1349 数据条数a
        try:
            s = df.loc[[i], [6]].values.tolist()[0][0]
            if s[-3:-1] == '下/':
                df.loc[[i], [6]] = int(eval(s[0]) * 10000 / 12)
                continue
            if s[-1] == '天':
                if s[-3] == '千':
                    df.loc[[i], [6]] = int(eval(s[0:-3]) * 1000 * 22)
                    continue
                elif s[-3] == '万':
                    df.loc[[i], [6]] = int(eval(s[0:-3]) * 10000 * 22)
                    continue
                else:
                    df.loc[[i], [6]] = int(eval(s[0:-3]) * 22)
                    continue
            if str(s) == 'nan':
                continue
            if str(s)[-1] == '下':
                w = re.search('([0-9]*[万千])', s)
                if str(w[0])[-1] == '万':
                    r = int(str(w[0])[0]) * 10000
                else:
                    r = int(str(w[0])[0]) * 1000
                value = round(r / 2)
                df.loc[[i], [6]] = value
            else:
                a = re.search('(.*)-([0-9.]*[\u4e00-\u9fa5])', str(s))[1]
                b = re.search('(.*)-([0-9.]*[\u4e00-\u9fa5])', str(s))[2]
                if b[-1] == '千':
                    x = eval(a[0:]) * 1000
                    y = eval(b[0:-1]) * 1000
                elif a[-1] == '千':
                    x = eval(a[0:-1]) * 1000
                    y = eval(b[0:-1]) * 10000
                elif b[-1] == '万':
                    x = eval(a[0:]) * 10000
                    y = eval(b[0:-1]) * 10000
                elif b[-1] == '年':
                    a1 = re.search('(.*)-(.*)\/年', str(s))[1]  # 处理年薪
                    b1 = re.search('(.*)-(.*)\/年', str(s))[2]
                    x1 = eval(a1[0:]) * 10000
                    y1 = eval(b1[0:-1]) * 10000
                    value1 = round((x1 + y1) / (2 * 12), -1)
                    df.loc[[i], [6]] = value1
                elif b[-1] == '薪':
                    m = re.search('(.*)-([0-9.]*[\u4e00-\u9fa5])', a)[1]
                    n = re.search('(.*)-([0-9.]*[\u4e00-\u9fa5])', a)[2]
                    if n[-1] == '千':
                        x = eval(a[0:]) * 1000
                        y = eval(b[0:-1]) * 1000
                    elif m[-1] == '千':
                        x = eval(a[0:-1]) * 1000
                        y = eval(b[0:-1]) * 10000
                    elif n[-1] == '万':
                        x = eval(a[0:]) * 10000
                        y = eval(b[0:-1]) * 10000
                    else:
                        print(s)
                        continue
                else:
                    print(s)
                    continue
                value = round((x + y) / 2)
                df.loc[[i], [6]] = value
        except:
            continue
    # nan字段填充
    # df[6]=pd.to_numeric(df[6], errors='coerce')#万能去除法，强制转换
    df[6].fillna(df[6].mean(), inplace=True)
    df[2].fillna('无需学历', inplace=True)
    df[3].fillna('其他', inplace=True)
    df[4].fillna('暂无', inplace=True)
    # 薪资数据转换
    df = df.astype({6: 'int'})
    df.reset_index(drop=True, inplace=True)
    for i in range(df.shape[0]):
        df[7][i] = df[7][i].replace("'", '')
    df.to_csv('static/data.csv', index=False, header=False, encoding='utf-8-sig')
    print('数据处理完毕！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')

if __name__ == '__main__':
    data_deal()