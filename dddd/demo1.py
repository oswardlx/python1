'''
第一个示例：简单的网页爬虫

爬取豆瓣首页
'''

import urllib.request
import re

#网址
# url = "https://www.8200.cn/kjh/ssq/history.htm?size=300"
# url = "https://www.8200.cn/kjh/ssq/history.htm"
url = "http://10.10.14.199/dsideal_yy/html/ypt/portals/qu_home.html?area_id=300529"
#请求
request = urllib.request.Request(url)

#爬取结果
response = urllib.request.urlopen(request)

data = response.read()

#设置解码方式
data = data.decode('utf-8')
print(data)
print(type(data))
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())
# reg=''
#打印结果
# key = r"(?<=<span class=\"text-red\">)" \
#       r"(?:.|[\r\n])*?</span>\+<span class=\"text-blue\">" \
#       r"(?:.|[\r\n])*?(?=</span>)"
# pattern1 = re.compile(key)
# # print( pattern1.findall(data)[0])
# matcher1 = re.search(pattern1,data)
# result = matcher1.group()
# space = result.replace("</span>+<span class=\"text-blue\">",'').replace("\r\n","")
# p =','.join(space.split())
# print(p)
# p1 = r"(?<=<h1>).+?(?=<h1>)"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
# pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
# matcher1 = re.search(pattern1, key)  # 在源文本中搜索符合正则表达式的部分
# print(matcher1.group(0))  # 打印出来

#打印爬取网页的各类信息



