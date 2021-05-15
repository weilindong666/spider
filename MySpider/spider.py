# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 13:04
# @Author  : Weilindong
# @File    : spider.py
# @Software: PyCharm


import urllib2
import urllib

#获取一个get请求
# response = urllib2.urlopen("https://www.baidu.com")
# print(response.read().decode("utf-8"))

#获取一个post请求
# data = bytes(urllib.urlencode({"hello": "word"}))
# response = urllib2.urlopen("https://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

#获取豆瓣网信息
def askURL(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"
    }
    req = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(req)
    return response

def getData(baseurl):
    for i in range(10):
        url = baseurl + str(i*25)
        html = askURL(url)

if __name__ == '__main__':
    url = "https://movie.douban.com/top250?start=0"
    # getData(url)
    html = askURL(url)
    print(html.read().decode("utf-8"))