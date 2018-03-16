import re

line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
# if matchObj:
#     print("matchObj.group():",matchObj.group())
#     print("matchObj.group(1):",matchObj.group(1))
#     print("matchObj.group(2):",matchObj.group(2))
#
# else:
#     print("No Match!!")
# print(re.search('www','www.runoob.com').span())
# print(re.search('com','www.runoob.com').span())
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print("match-->matchobj.group():", matchObj.group())
# else:
#     print("No match!!")
# matchObj = re.search( r'dogs', line, re.M|re.I)
# if matchObj:
#     print("search --> matchObj.group() : ", matchObj.group())
# else:
#     print( "No match!!")
ballinfo = "<span class=\"text-red\">\n06\n15\n26\n31\n32\n33\n</span>"
# ballinfo = ballinfo.replace('\t','').replace('\n','').replace(' ','')

print(ballinfo)
key = r"<span[^>]*>(?:.|[\r\n])*?</span>"
pattern = re.compile(key)
result = pattern.findall(ballinfo)
print(result)
# phone ="2004-959-559 # 这是一个国外电话号码"
# num = re.sub(r'#.*$',"",phone)
# print("电话号码是：",num)