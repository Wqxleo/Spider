from urllib import request, parse

s = "年 货"
# result = request.quote(s)
result = parse.quote_plus(s)
print(result)
# de = request.unquote(result)
# print(de)