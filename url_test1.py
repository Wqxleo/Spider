from urllib import request

file = request.urlopen("http://www.baidu.com")
content = file.read().decode("utf-8")
print(content)