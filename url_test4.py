from urllib import request, parse

data = {'did': 6}
data = parse.urlencode(data)
file = request.urlopen("http://www.dycollege.net/dept?%s"%data)
content = file.read().decode("utf-8")
print(content)