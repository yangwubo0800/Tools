import requests
from lxml import etree
import re
import json
import csv
import time
import random


headers = {
    'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    #设置登录后自己账号的cookie
    'Cookie': 'JSESSIONID=D2F496D4EDD1283BB38993A300479625; td_cookie=2022463651; avatarImageUrl=-838844014974055970; _jzqx=1.1551864649.1551864649.1.jzqsr=cshnac%2Ecom|jzqct=/.-; login_locale=zh_CN; _jzqa=1.3604929142647255000.1551864649.1551864649.1564395902.2; _jzqc=1; Hm_lvt_31f37542580c45a60f3d9c3cc4038b53=1564395902; Hm_lpvt_31f37542580c45a60f3d9c3cc4038b53=1564395902; loginPageURL='
}
#爬取加班页面内容
def get_page(url):
    print('爬取页面:')
    print(url)
    response = requests.get(url=url,headers=headers)
    html = response.text
    return html
#获取已发事项列表数据
def get_data():
    print('开始获取列表数据...')
    #已发事项分页获取后台数据接口url
    url='http://oa.cshnac.com:8088/seeyon/ajax.do?method=ajaxAction&managerName=colManager&rnd=14803'
    data={
    'managerMethod':'getSentList',
    #设置自己需要一次爬取的条数，此处设置为一次300条
	'arguments':'[{"page":1,"size":"300"},{}]'
    }
    response = requests.post(url=url,headers=headers,data=data)
    jsonData = response.text
    print(jsonData)
    return jsonData
    #fm = input('请输入文件保存格式（txt、json、csv）：')
    #while fm!='txt' and fm!='json' and fm!='csv':
        #fm = input('输入错误，请重新输入文件保存格式（txt、json、csv）：')
    #fd = openfile(fm)
    #print('开始保存')
    #saveJsonData2file(fm,fd,jsonData)
    #responseData = json.loads(jsonData)
    #print(responseData['data'][0]['summaryId'])
# 解析网页源代码，获取加班申请表格中的数据
def parse4data(html):
    html = etree.HTML(html)
    proposer = html.xpath('//span[@id="field0010_span"]/span/text()')
    startTime = html.xpath('//span[@id="field0016_span"]/span/text()')
    endTime = html.xpath('//span[@id="field0013_span"]/span/text()')
    content = html.xpath('//span[@id="field0006_span"]/span/text()')
    duration = html.xpath('//span[@id="field0004_span"]/span/text()')
    data = zip(proposer,startTime,endTime,content,duration)
    print('解析页面数据')
    print(proposer)
    return data
# 打开文件
def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('hzsent.txt','w',encoding='utf-8')
    elif fm == 'json':
        fd = open('hzlist.json','w',encoding='utf-8')
    elif fm == 'csv':
        fd = open('hzsent.csv','w',encoding='utf-8',newline='')
    return fd

# 将数据保存到文件
def save2file(fm,fd,data):
    if fm == 'txt':
        for item in data:
            fd.write('----------------------------------------\n')
            fd.write('proposer：' + str(item[0]) + '\n')
            fd.write('startTime：' + str(item[1]) + '\n')
            fd.write('endTime：' + str(item[2]) + '\n')
            fd.write('content：' + str(item[3]) + '\n')
            fd.write('duration：' + str(item[4]) + '\n')
    if fm == 'json':
        temp = ('link','title','role','descrition','star','comment')
        for item in data:
            json.dump(dict(zip(temp,item)),fd,ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)
            
def saveJsonData2file(fm,fd,data):
    if fm == 'txt':
        fd.write(data)
    if fm == 'json':
        temp = ('link','title','role','descrition','star','comment')
        for item in data:
            json.dump(dict(zip(temp,item)),fd,ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)
# 开始爬取网页
def crawl():
    #各个加班申请页面的url，其中的moduleId参数及为前面获取json数据中的SummeryId
    url = 'http://oa.cshnac.com:8088/seeyon/content/content.do?method=index&isFullPage=true&hasDealArea=false&moduleId={summaryId}&moduleType=1&rightId=8290946041593414956.2450333582631322767&contentType=20&viewState=2&openFrom=listSent&canDeleteISigntureHtml=false&isSubFlow=&isShowMoveMenu=false&isShowDocLockMenu=false&rnd=1564804267504'
    fm = input('请输入文件保存格式（txt、json、csv）：')
    while fm!='txt' and fm!='json' and fm!='csv':
        fm = input('输入错误，请重新输入文件保存格式（txt、json、csv）：')
    fd = openfile(fm)
    jsonData = get_data()
    listData = json.loads(jsonData)
    print('=====start get summaryId')
    #print(listData['data'][0]['summaryId'])
    summaryIds = [d['summaryId'] for d in listData['data']]
    print(summaryIds)
    for summaryId in summaryIds:
        html = get_page(url.format(summaryId=summaryId))
        htmlData = parse4data(html)
        save2file(fm,fd,htmlData)
        time.sleep(random.random())
    fd.close()
    print('结束爬取')

if __name__ == '__main__':
    crawl()
    #get_data()