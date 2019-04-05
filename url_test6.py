from urllib import request
import webbrowser

# request.urlretrieve("https://img1.doubanio.com/view/note/large/public/p56831139.jpg", 'img/p56.jpg')
webbrowser.open("http://www.baidu.com")

# 1. 爬取豆瓣电影首页（正在热映或最近热门电影）板块的电影海报、电影名称及评分
# 2. 将爬取到的资源写入html页面，生成“我的热门电影”页面
# 3. 自动打开该页面
