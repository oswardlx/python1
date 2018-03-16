import re

key = r"<html><body><h1>hello world<h1></body></html>"  # 这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=<h1>)"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
matcher1 = re.search(pattern1, key)  # 在源文本中搜索符合正则表达式的部分
print(matcher1.group(0))  # 打印出来


p2 = r"<h1>.+<h1>"
parttern2 = re.compile(p2)
print(parttern2.findall(key))

key2 = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
p3 = r"chuxiuhong@hit\.edu\.cn"
pattern3 = re.compile(p3)
print(pattern3.findall(key2))

key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"#胡编乱造的网址，别在意
p1 = r"https*://"#看那个星号！
pattern1 = re.compile(p1)
print (pattern1.findall(key))

key = r"lalala<hTml>hello</Html>heiheihei"
p1 = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"
pattern1 = re.compile(p1)
print (pattern1.findall(key))

key = r"mat cat hat pat"
p1 = r"[^p]at"#这代表除了p以外都匹配
pattern1 = re.compile(p1)
print( pattern1.findall(key))

key = "<span class=\"text-red\">\n01\n02\n09\n14\n22\n25</span>"
p2 = ">[0-9]{12}<"
pattern1 = re.compile(p2)
print( pattern1.findall(key))
