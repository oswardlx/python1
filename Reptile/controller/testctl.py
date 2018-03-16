
from Reptile.service.analysisData import *
from Reptile.data.getDataFromUrl import *
# url = "https://www.8200.cn/kjh/ssq/history.htm"
url="http://10.10.14.199/dsideal_yy/html/ypt/portals/qu_home.html?area_id=300529"
# data = GetAddSql(url)
data1 = GetDataFromUrl(url)
result1 = data1.get_url_data()
# result = data.get_data_pre_format()
print(result1)