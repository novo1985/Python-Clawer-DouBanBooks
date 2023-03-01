# 网页使用utf-8编码
# https://www.baidu.com/s?wd=中
# 上面的url编码后，如下：（从浏览器复制粘贴到IDE中的显示）
# https://www.baidu.com/s?wd=%E4%B8%AD

from urllib import parse

u = parse.urlencode({'wd': '中'})
url = "https://www.baidu.com/s?{}".format(u)
print(url)

print('中'.encode('utf-8'))

# 解码
print(parse.unquote(u))
print(parse.unquote(url))

# dic = {
#     'id': 1,
#     'name': 'Leo',
#     'url': 'https://www.youtube.com/watch?id=1&name=Leo'
# }
# str = parse.urlencode(dic)
# print(str)

# url = 'https://www.youtube.com/watch?id=1&name=Leo'  # GET method
# url = 'https://www.youtube.com/watch'  # POST method
# body = 'id=1&name=Leo'

# Part2
# https://www.bing.com/search?q=%E9%A9%AC%E5%93%A5%E6%95%99%E8%82%B2 (马哥教育)
base_url = 'https://www.bing.com/search'

search_dic = {
    'q': '马哥教育'
}

# 将search的部分安全编码
url_q = parse.urlencode(search_dic)
final_url = '{}?{}'.format(base_url, url_q)

print(final_url)
print(parse.unquote(final_url))

from urllib.request import urlopen, Request

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19042'

req = Request(final_url, headers={
    'User-agent': ua
})

res = urlopen(req)
with res:
    with open('c:/Users/leoge/Downloads/bing.html', 'wb+') as f:
        f.write(res.read())
        f.flush()

print("Done!")



