from urllib import request, parse
import requests

data = {'source': 'index_nav', 'form_email': 'chris19901013@163.com', 'form_password': 'Chen1990'}
url = "https://www.douban.com/accounts/login"
# 数据编码
# data = parse.urlencode(data).encode("utf-8")
# file = request.urlopen(url, data=data)
# content = file.read().decode("utf-8")
# print(content)

file = requests.post(url, data=data)
print(file.text)

# 第三方库模拟登录
