# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 13:09
# @Author  : Weilindong
# @File    : testBS4.py
# @Software: PyCharm


from bs4 import BeautifulSoup

#Tag是标签及其内容，默认找到第一个项目

if __name__ == '__main__':
    file = open("./douban.html", "rb")
    html = file.read()
    bs = BeautifulSoup(html, "html.parser")
    print(bs.link)