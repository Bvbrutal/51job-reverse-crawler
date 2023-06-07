import hmac
import random
import time
from urllib import parse
import requests
from hashlib import sha256

User_Agent = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR "
    "2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center "
    "PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET "
    "CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR "
    "3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR "
    "2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; "
    ".NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
    "Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 "
    "Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 "
    "Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 "
    "TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 "
    "Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 "
    "Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; "
    "360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET "
    "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) "
    "Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 "
    "Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) "
    "Firefox/3.6.10 "
]

def get_sign(data):
    key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    sign = hmac.new(key, message, digestmod=sha256).hexdigest()
    return sign


def get_search(keyword, num):
    timestamp = int(time.time())
    key = parse.quote(keyword)
    # https://cupidjob.51job.com/open/noauth/search-pc?api_key=51job&timestamp=1683218964&keyword=python&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=221776941&pageCode=sou%7Csou%7Csoulb
    url = f'https://cupidjob.51job.com/open/noauth/search-pc?api_key=51job&timestamp={timestamp}&keyword=python&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=3&requestId=3fb827a9efe06de56197d23955b5a644&pageSize=20&source=1&accountId=221776941&pageCode=sou%7Csou%7Csoulb'
    path = parse.urlparse(url)
    paths = path.path + '?' + path.query
    sign = get_sign(paths)
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'account-id': '221776941',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'guid=ef1964290e5ac54e29db9610d5eceec5; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; sensor=createDate%3D2023-02-14%26%7C%26identityType%3D2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22221776941%22%2C%22first_id%22%3A%22186c73386d4511-0330cfe3e81ee72-74525476-1327104-186c73386d51106%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2YzczMzg2ZDQ1MTEtMDMzMGNmZTNlODFlZTcyLTc0NTI1NDc2LTEzMjcxMDQtMTg2YzczMzg2ZDUxMTA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjIxNzc2OTQxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22221776941%22%7D%2C%22%24device_id%22%3A%22186c73386d4511-0330cfe3e81ee72-74525476-1327104-186c73386d51106%22%7D; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1683218119; 51job=cuid%3D221776941%26%7C%26cusername%3DWuPP4rj0WxSFYfhrvqigZ%252FwM1laAjwwKa5G8%252BO1view%253D%26%7C%26cpassword%3D%26%7C%26cname%3DADtLAWvQCfLuCiC5V6gXEg%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0b2J6DLkq8ak%26%7C%26cconfirmkey%3D%25241%252461j0aYJC%2524eASxTq2WF98Mez21QoWFp0%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%2524Phsam3GO%252440EWa7BIxZXS5YhlhVP941%26%7C%26to%3D0a9915c9c4d6a7e11c6ef3e37500eb1e6453ded0%26%7C%26; privacy=1683218128; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1683218130; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20230505%26%7C%26securetime%3DUGxSZ1A%252BBGNXNwQ7WmkIYlNjCjs%253D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CF%FA%CA%DB%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_tc=ac11000116832181377624006e00dd83990bd91971a37f8ab58a4c0e1ef1bd; uid=wKhJPmRT3tpcrgMcBT3QAg==; JSESSIONID=A5A38F391E863A672BFFEDAE0443664D; ssxmod_itna=YqRxyiDQD=KGqYIP0LPC4x9BDuQGtqOqoCOTCr7DlxxWueGzDAxn40iDt=aXBmQhnDHoC77Prt7CO8pwQdFZYwWHrTj4YepDU4i8DCuue5TDeWtD5xGoDPxDeDAmqGaDb4Dr9=qGpycukXybqGRD0YDzqDgD7Q45eDfDDLynGAyGnLy0udPomrDAwqlGD+yD0tDIqGXCOcezqDB7ccelqXrdPGWFo=ereGuDG656qQKx0PgDWNun=AAKG4GKAQH8hqiY7hbG4pjTYq4/7hTeE84BGG6dM46IYxDG4+eUG4YeD===; ssxmod_itna2=YqRxyiDQD=KGqYIP0LPC4x9BDuQGtqOqoCOTCrD6E4pQjjD05H=03YK9siKuD6Q0F4kemx2Kb5RDWw=t973w00+R48M5biOU+ekHjeHf=LbOe5wUfLez6poEhy4vTmelcCiti8OttOHbo=wi8mbb37ebe=viVipK5pptiYcHsmGqPp0Cs6cpagOa0QorhZgtbF91D2BTU28bhoerblFwB8p79i9L/FP09S3EFALslxcfYORjLor4t2WKKaKeZrexWsa6gO1Cmc=0HyMaiEKFiC9NvM6ikKz0IwTgRbKWta1y/o/kGLd0FiZi+D50DzwdGuxpcRQuDyrzYRyFw6S+eHyXFTOQAKNwes5DsqF+HOmRPyaK24MfywFHdw+Yr+rtOqVTcbcz+EyRB52hUnvlto03ubtEP1BiguQe85oWTPm=k8bdyohh3D07FfxdStq7TMoqG8L5hNzZo8iIiBYy2Dexjkb1r0TlE6v1qe+oD7=DYF4eD===',
        'From-Domain': '51job_web',
        'Host': 'cupidjob.51job.com',
        'Origin': 'https://we.51job.com',
        'Pragma': 'no-cache',
        'property': '%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D060000%26keyword%3D%25E5%25B8%2588%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%E5%9C%A8%E6%A0%A1%E7%94%9F%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22221776941%22%7D',
        'Referer': 'https://we.51job.com/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'sign': sign,
        'User-Agent': random.choice(User_Agent),
        'user-token': '0a9915c9c4d6a7e11c6ef3e37500eb1e6453ded0',
        'uuid': 'ef1964290e5ac54e29db9610d5eceec5',
    }
    result = requests.get(url=url, headers=header)
    print(result.text)
    data_result = result.json()
    return data_result


if __name__ == '__main__':
    get_search('python', 5)
