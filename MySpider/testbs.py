# -*- coding: utf-8 -*-
"""
@Time    : 2021/5/15 12:59
@Author  : Weilindong
@File    : testbs.py
@Software: PyCharm
"""

from bs4 import BeautifulSoup

file = open("./douban.html", "rb")
html = file.read().decode("utf-8")

bs = BeautifulSoup(html, "html.parser")

# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("link")
print(t_list)

# 正则表达式搜索： 使用search（）方法来匹配内容
import re

f_list = bs.find_all(re.compile("link"))
print(f_list)


# 方法 ： 传入一个函数（方法）， 根据函数的要求进行搜索
def name_is_exists(tag):
    return tag.has_attr("href")


k_list = bs.find_all(name_is_exists)
print(k_list)

# kwargs: 参数
# l_list = bs.find_all(id="footer")
l_list = bs.find_all(class_="extra")
print(l_list)
# print(bs)

# text 参数
# o_list = bs.find_all(text="豆瓣广告")
# o_list = bs.find_all(text=["移动应用", "豆瓣广告"])
o_list = bs.find_all(text=re.compile("\d")) #应用正则表达式查找包含特定文本的内容（此代码表示包含数字的内容）
for i in o_list:
    print(i)
