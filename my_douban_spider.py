"""
@author:  wangquaxiu
@time:  2019/1/19 16:35
"""
from _tracemalloc import start
from urllib import request
from lxml import etree
import os
url = 'https://movie.douban.com'
html = request.urlopen(url)
contents = html.read().decode('utf-8')

# 构造了一个XPath解析对象并对HTML文本进行自动修正
contents = etree.HTML(contents)

datas = contents.xpath('//ul[@class="ui-slide-content"]/li')
movies = []
for data in datas:
    movie = []
    movie_title = data.xpath('ul/li/a/img/@alt')
    movie_img = data.xpath('ul/li/a/img/@src')
    movie_rate = data.xpath('ul/li[3]/span[2]/text()')

    # movie.append(movie_title)
    # movie.append(movie_img)
    # movie.append(movie_rate)
    # movies.append(movie)
    # print(movie)

    if len(movie_title) != 0:
        movie.append(movie_title[0])
    else:break

    movie.append(movie_img[0])
    # print(data.xpath('ul/li/a/img/@alt'))
    if len(movie_rate) != 0:
        movie.append(movie_rate[0])
    else:movie.append('暂无')
    print(movie)
    movies.append(movie)
# print(movies)

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Movies</title>
</head>
<body>
<h1>
    热映影片
</h1>"""
html_body = '\n'
for movie in movies:
    html_body += ("""<p>"""+'\n')
    html_body += ("片名: "+movie[0]+"""<img src=\""""+movie[1]+"""\">"""+"评分："+movie[2]+'\n')
    html_body += ("""</p>"""+'\n')

html_end = """</body>
</html>"""

my_html = open("G:/Python/first_spider/html_dir/my_ht.html",'w',encoding='utf-8')
my_html.write(html_head+html_body+html_end)
my_html.close()

os.system("C:/Users/wangq/AppData/Local/Google/Chrome/Application/chrome.exe G:/Python/first_spider/html_dir/my_ht.html")

