import requests
from lxml import etree
import re
import json
import csv
import time
import random

# 获取网页源代码
def get_page(url):
    headers = {
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'bid=KoKETvZKhFc; __yadk_uid=GBzoWKNHXeLtMYlAMhFlf4QX5WzZZN98; trc_cookie_storage=taboola%2520global%253Auser-id%3Dc79dfdc4-841c-4704-9829-1d598c16b7d7-tuct485930d; ll="118267"; ap_v=0,6.0; __utma=30149280.1080961294.1568095494.1570843733.1571013461.3; __utmc=30149280; __utmz=30149280.1571013461.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1877907612.1570843733.1570843733.1571013463.2; __utmb=223695111.0.10.1571013463; __utmc=223695111; __utmz=223695111.1571013463.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1571013463%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _vwo_uuid_v2=D6B2F8120BF60FDF208083D1BCA4B45CC|4ee242095372de682d8a6307bd027fdc; __utmt=1; __gads=ID=8294a42f25bf23ff:T=1571014175:S=ALNI_MaciOALyqhD7zoW7uIMZY4fl0pZXQ; __utmb=30149280.3.10.1571013461; dbcl2="159219919:RJ7RM7vBqNA"; ck=Wivv; _pk_id.100001.4cf6=cd023146861ac142.1570843733.2.1571014623.1570843733.; push_noty_num=0; push_doumail_num=0'
    }
    response = requests.get(url=url,headers=headers)
    html = response.text
    return html

# 解析网页源代码，获取下一页链接
def parse4link(html,base_url):
    link = None
    html_elem = etree.HTML(html)
    url = html_elem.xpath('//div[@id="paginator"]/a[@class="next"]/@href')
    if url:
        link = base_url + url[0]
    return link

# 解析网页源代码，获取数据
def parse4data(html):
    html = etree.HTML(html)
    agrees = html.xpath('//div[@class="comment-item"]/div[2]/h3/span[1]/span/text()')
    authods = html.xpath('//div[@class="comment-item"]/div[2]/h3/span[2]/a/text()')
    stars = html.xpath('//div[@class="comment-item"]/div[2]/h3/span[2]/span[2]/@title')
    contents = html.xpath('//div[@class="comment-item"]/div[2]/p/span/text()')
    data = zip(agrees,authods,stars,contents)
    return data

# 打开文件
def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('douban_comment.txt','w',encoding='utf-8')
    elif fm == 'json':
        fd = open('douban_comment.json','w',encoding='utf-8')
    elif fm == 'csv':
        fd = open('douban_comment.csv','w',encoding='utf-8',newline='')
    return fd

# 将数据保存到文件
def save2file(fm,fd,data):
    if fm == 'txt':
        for item in data:
            fd.write('----------------------------------------\n')
            fd.write('agree：' + str(item[0]) + '\n')
            fd.write('authod：' + str(item[1]) + '\n')
            fd.write('star：' + str(item[2]) + '\n')
            fd.write('content：' + str(item[3]) + '\n')
    if fm == 'json':
        temp = ('agree','authod','star','content')
        for item in data:
            json.dump(dict(zip(temp,item)),fd,ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)

# 开始爬取网页
def crawl():
    moveID = input('请输入电影ID：')
    while not re.match(r'\d{7}',moveID):
        moveID = input('输入错误，请重新输入电影ID：')
    base_url = 'https://movie.douban.com/subject/' + moveID + '/comments'
    fm = input('请输入文件保存格式（txt、json、csv）：')
    while fm!='txt' and fm!='json' and fm!='csv':
        fm = input('输入错误，请重新输入文件保存格式（txt、json、csv）：')
    fd = openfile(fm)
    print('开始爬取')
    link = base_url
    while link:
        print('正在爬取 ' + str(link) + ' ......')
        html = get_page(link)
        link = parse4link(html,base_url)
        data = parse4data(html)
        save2file(fm,fd,data)
        time.sleep(random.random())
    fd.close()
    print('结束爬取')

if __name__ == '__main__':
    crawl()
