import hmac
import random
import time
from hashlib import sha256
from urllib import parse
import pandas as pd
from lxml import etree
import execjs
import requests
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
class wuyou():
    def __init__(self):
        self.requestid=['']
    def get_search(self,keyword,num):
        time.sleep(random.random() * 2)
        timestamp=int(time.time())
        key=parse.quote(keyword)
        # https://cupidjob.51job.com/open/noauth/search-pc?api_key=51job&timestamp=1683218964&keyword=python&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=1&requestId=&pageSize=20&source=1&accountId=221776941&pageCode=sou%7Csou%7Csoulb
        url = f'https://cupidjob.51job.com/open/noauth/search-pc?api_key=51job&timestamp={timestamp}&keyword={key}&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum={num}&requestId={self.requestid[-1]}&pageSize=50&source=1&accountId=221776941&pageCode=sou%7Csou%7Csoulb'
        path=parse.urlparse(url)
        paths=path.path+'?'+path.query
        sign = self.get_sign(paths)
        header = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'account-id': '221776941',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'From-Domain': '51job_web',
            'Host': 'cupidjob.51job.com',
            'Origin': 'https://we.51job.com',
            'partner': '',
            'Pragma': 'no-cache',
            'property': '%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3FjobArea%3D060000%26keyword%3D%25E5%25B8%2588%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%E5%9C%A8%E6%A0%A1%E7%94%9F%22%2C%22userType%22%3A%22%E8%80%81%E7%94%A8%E6%88%B7%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22221776941%22%7D',
            'Referer': 'https://we.51job.com/',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': random.choice(User_Agent),
            'user-token': '239029340688adf28b1382a1565e1f7264061e22',
            'uuid': '1abe6d99b542705b5cd4c550655c6b33',
            'sign':f'{sign}',
            'Cookie': 'guid=ef1964290e5ac54e29db9610d5eceec5; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1683218119,1683794886; 51job=cuid%3D222996194%26%7C%26cusername%3DHk57Sng%252B2KPVDmjJfEYR4kADEvTy%252BSL3uAyN2YArJCU%253D%26%7C%26cpassword%3D%26%7C%26cname%3D9CefG4ZfKhgdrcDm5w%252B40A%253D%253D%26%7C%26cemail%3D5R1LMkIWMYd1soE42kcGvuIGFurvXhvQJtT3eHT47wk%253D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.02JxBb0gu6Kg%26%7C%26cconfirmkey%3D10.NIkATCsWsI%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D10eM51wn9Z%252FnU%26%7C%26to%3Da08136f26d9abde3b5e7ca8718f383fe645cac09%26%7C%26; sensor=createDate%3D2023-03-01%26%7C%26identityType%3D2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22222996194%22%2C%22first_id%22%3A%22186c73386d4511-0330cfe3e81ee72-74525476-1327104-186c73386d51106%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2YzczMzg2ZDQ1MTEtMDMzMGNmZTNlODFlZTcyLTc0NTI1NDc2LTEzMjcxMDQtMTg2YzczMzg2ZDUxMTA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjIyOTk2MTk0In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22222996194%22%7D%2C%22%24device_id%22%3A%22186c73386d4511-0330cfe3e81ee72-74525476-1327104-186c73386d51106%22%7D; acw_tc=ac11000116856148459418506e00e114d3d3b6080618e7bf3b3c30b7ad2c41; slife=securetime%3DADxcaVg2VzYCZlRrWmUMb1FmUWA%253D; acw_sc__v2=6478710447fc74a66409594751877d259bd677d3; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%B8%DF%BC%B6%BF%AA%B7%A2%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA03%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA02%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=0B67FF5A728287EF453BD177C0C89F03; ssxmod_itna=YqAO7KAIx0hx7bDXYG7maG=jWUb7RKiUKfUfDBL84iNDnD8x7YDvm+xsmKzKbz0D0=EDzDT+qObP+ifQ4Omb74vNb6M4GLDmKDytQi4qoD4fKGwD0eG+DD4DWDmmHDnxAQDjxGPyn2v5CDYPDEBKDaxDbDimkAxGCDeKD0Z4HDQKDug9+CZB1HFyxdz+kD7HIDla4E/GkTf3LNny+wz4hEGKDXEdDvpy1/gcpDBbCVE5hlBWxbjTqbm035WxqDmqxNAexbAD9emriYirNHTD9zGhufVDDia2qpGhDD==; ssxmod_itna2=YqAO7KAIx0hx7bDXYG7maG=jWUb7RKiUKffD8qpBxY54D/tBDFOBgwzgqU+KBK86SrMD6Qe5iwxj59WfEg2F9tYcyNEeRiwvXTWN7coF+VBFo2cFCdiQ62qazsiow2SiM9OMgm1SKD6BT45BnNYDuGneA4DEAbmPTG3PAPdxow/0epQUPI1Seve07h5E74Q8evKP74mRoH1ROpeDL+mtL+Rb3bURBDW=nX1Iaw8RDAgU3f8zkGokEtBR7Rqyf1W5YHCIS+jSoAr48LKOQEp679kyPAEI3BQsQEf2tHqTSSnqfNLLnSZMWfTYO+WKu5RdGCR5NMs4ehlL1rOrkb3mEz/BiHhGd4iqMdrehqirGQ=Obw1R5quhKq31gx=wi33tN3p+T+YhQ7bvQ2olr33Etkjv6keFCv9AY/E1z7wrxi1oKipAamvqZf/lWiZEopLb4A1oqADDwZqPmp3DAkAneiPuIDn9Xc3v93m5DGcDG7NiDD=='
        }
        result=requests.get(url=url, headers=header)
        print(result.text)
        data_result=result.json()
        return data_result

    def analyzy(self,data,m):
        lists = []
        for datas in data["resultbody"]["job"]["items"]:
            jobname=datas["jobName"]
            jobAreaString=datas['jobAreaString']
            provideSalaryString=datas['provideSalaryString']
            degreeString=datas['degreeString']
            fullCompanyName=datas['fullCompanyName']
            companyTypeString=datas['companyTypeString']
            termStr=datas['termStr']
            jobHref=datas['jobHref']
            jobTags=datas['jobTags']
            updateDateTime=datas['updateDateTime']
            industryType1Str=datas['industryType1Str']
            workYearString=datas['workYearString']
            companySizeString=datas['companySizeString']
            jobtag=str(jobTags).replace('[','').replace(']','')#简单数据处理：除掉[]
            listss = [fullCompanyName,jobname,degreeString,companyTypeString,companySizeString,jobAreaString,provideSalaryString,jobtag,workYearString,termStr,updateDateTime,industryType1Str]
            lists.append(listss)
            m-=1
            print('公司全称：{:<}   岗位名称：{:<}   公司规模：{:<}  城市：{:<}  公司规模：{:<} 职位标签：{:<}  工作时间：{:<}'.format(fullCompanyName,jobname,companySizeString,jobAreaString,provideSalaryString,jobtag,termStr))
            # 爬内页
            # self.get_detail(jobHref)
        return lists,m

    def get_sign(self,data):
        key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'
        key = key.encode('utf-8')
        message = data.encode('utf-8')
        sign = hmac.new(key, message, digestmod=sha256).hexdigest()
        return sign
    # def get_neiye(self):

    def get_detail(self,url,retry=0):
        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control':'no-cache',
            'Connection':'keep-alive',
            'Cookie':'_uab_collina=167773914485564744472978; guid=1abe6d99b542705b5cd4c550655c6b33; ps=needv%3D0; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; adv=ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fpartner%253Dsem_pcbaiduqg_15730%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIwXzEuaHRtbD9mcm9tPWJhaWR1YWQmcGFydG5lcj1zZW1fcGNiYWlkdXFnXzE1NzMw%2526k%253D76316c579c393a854a7a88ed42a2cb80%2526bd_vid%253D7950813595915875330%26%7C%26; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1677662231,1677739020,1678122457; 51job=cuid%3D221776941%26%7C%26cusername%3DWuPP4rj0WxSFYfhrvqigZ%252FwM1laAjwwKa5G8%252BO1view%253D%26%7C%26cpassword%3D%26%7C%26cname%3DADtLAWvQCfLuCiC5V6gXEg%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0b2J6DLkq8ak%26%7C%26cconfirmkey%3D%25241%252426ZU9%252FjW%2524OPDC6np74gPR5ZN7Pvu51.%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%2524bjQTX%252FFT%25243olMnkOp9gB58Ue0OCThm0%26%7C%26to%3D239029340688adf28b1382a1565e1f7264061e22%26%7C%26; sensor=createDate%3D2023-02-14%26%7C%26identityType%3D2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22221776941%22%2C%22first_id%22%3A%221869c761ae4bcf-09a2610ff16439-74525471-1327104-1869c761ae5675%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2OWM3NjFhZTRiY2YtMDlhMjYxMGZmMTY0MzktNzQ1MjU0NzEtMTMyNzEwNC0xODY5Yzc2MWFlNTY3NSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjIyMTc3Njk0MSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22221776941%22%7D%2C%22%24device_id%22%3A%221869c761ae4bcf-09a2610ff16439-74525471-1327104-1869c761ae5675%22%7D; search=jobarea%7E%60060000%7C%21recentSearch0%7E%60060000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60060000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%E8%BC%C6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60060000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C9%E8%BC%C6%A1%A2%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60060000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20230308%26%7C%26securetime%3DUm4HMlEwWDQAYAM4ATsJYAY3BzI%253D; privacy=1678276937; acw_tc=ac11000116782835648057105e00e1f992ff8df6750369a6ca1b2f30d63ec8; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1678283566; ssxmod_itna=QqGxcQG=0=D=GQqDtDX8G7AHIlo5Kooe=e8=DgAx0ypxPGzDAxn40iDtrryYO/iBhx4bFj8BD=Ybjbb+K6br7c4qiv83qGLDmKDyKlGbPDxhq0rD74irDDxD3BD7PGmDie1RD7EZlMgkMQD3qDwDB=DmqG2eQiDA4Dj8kwh8urU8utUiWiPxGUxjM+d8qDMD7tD/RGWoA=DGTaFoGNM41WDbOpuQniDtqD98mtXWeDHGuNlYqH3zDfvEBv3QApxUi4W3rhKA7GLoYxWzB+Kb0MPYvhKUUMQzH8DGS44R0mxeD===; ssxmod_itna2=QqGxcQG=0=D=GQqDtDX8G7AHIlo5Kooe=e8=DgDnISPxfeDsbdqDLD3OsohheqApd9Y7uDhGqdt7ib+9zm0O2d0+ZBEhK==lCTjd=joCy+7kZ8txFG+VI7YiWpwOY/PjHW5V20yyDfDSzAdhSbXLKdNED4dfYDoh7MKOmT21+Chd+k=Aioxq+EAp4SxjedWhewRbPdXYvBoK=ZE3PjAOOkA3E=ikioE+8nKu8W72fmv2S3gBitAgl67HKdx+qb5G7KM2zFAPKM4Fx4CGjURjvw24ZUC1fWQu6x/UvNA4vwz66OZ2Dy9SEX6oNROXZ6NZg6BoKK15qKX2xYj0LdrrRlPRiIKKtqS0madvQjNFmNtj=bKD+Rit2EjwTSvKmAplG7CqbzKizwhYPL2bHOXaxn17N02084PM1qFfum+WOB5MpvsxIh8Kpjw7bPClWifaqefLtDLIp7zc5W9vWDfbbEAcrjFH4Hcfcxmch/9LIDaDG2i4DFqD+he40wKjDWW9de4xD===',
            'Host':'jobs.51job.com',
            'Pragma':'no-cache',
            'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'none',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': random.choice(User_Agent),
        }
        with open('time_.js', 'r', encoding='utf-8') as f:
            fu_ = f.read()
        ctx = execjs.compile(fu_)
        pathname = parse.urlparse(url).path
        time_ = ctx.call('get_time_',url,pathname)
        params = {
                "timestamp__1258": time_
        }
        proxies = [{'https':'103.165.244.122:3128'},{'https':'111.225.153.15:8089'},{'https':'103.179.182.185:8181'},{'https':'171.240.91.137:4009'},{'https':'157.100.13.204:999'},{'https':'111.225.153.48:8089'},{'https':'111.224.11.206:8089'},{'https':'14.207.150.155:8080'},{'https':'27.157.225.153:8089'},{'https':'59.59.215.203:8089'},{'https':'59.59.214.121:8089'},{'https':'59.59.213.51:8089'},{'https':'183.165.250.50:8089'},{'https':'27.157.230.144:8089'},{'https':'49.88.158.119:8089'},{'https':'49.88.158.151:8089'},{'https':'14.18.63.228:8888'},{'https':'175.9.236.126:7890'},{'https':'175.9.239.215:7890'},{'https':'49.89.103.251:8089'}]
        proxy = random.choice(proxies)
        try:
            response = requests.get(url, headers=header, params=params,proxies=proxy)
            response.encoding = response.apparent_encoding
            html = etree.HTML(response.text)
            print(response)
            job_info = ''.join(html.xpath('//div[@class="bmsg job_msg inbox"]//text()')).strip().replace('\r\n', '').replace(' ', '')  # 职位描述
            print(job_info)
        except:
            retry += 1
            print(f"请求失败--重试第{retry}次")
            if retry < 20:
                self.get_detail(url, retry=retry)
    def data_tocsv(self,key,page):
        response = self.get_search(key, 1)
        m = response["resultbody"]["job"]['totalCount']
        datas, m = self.analyzy(response, m)
        for i in range(2,page):
            response=self.get_search(key,i)
            data,m=self.analyzy(response,m)
            datas+=data
            if m==0:
                break
        df = pd.DataFrame(datas)
        df.to_csv('static/data.csv',mode='a', index=False, header=False,encoding='utf-8-sig')

if __name__ == '__main__':
    wy = wuyou()  # 实例化
    wy.get_search('python',2)