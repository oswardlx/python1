# url = "https://www.8200.cn/kjh/ssq/history.htm?size=300"
from Reptile.data.getDataFromUrl import *
import re


class GetAddSql(object):
    def __init__(self, url):
        self.url = url

    def get_data_pre_format(self):
        data = GetDataFromUrl(self.url)
        result = data.get_url_data()
        return self.format_result(result)

    def format_result(self, data):
        key = r"(?<=<span class=\"text-red\">)" \
              r"(?:.|[\r\n])*?</span>\+<span class=\"text-blue\">" \
              r"(?:.|[\r\n])*?(?=</span>)"
        pattern1 = re.compile(key)
        matcher1 = re.search(pattern1, data)
        result = matcher1.group()
        space = result.replace("</span>+<span class=\"text-blue\">", '').replace("\r\n", "")
        p = ','.join(space.split())
        return p
