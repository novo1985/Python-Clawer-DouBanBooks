import urllib3
from urllib.parse import urlencode
from urllib3.response import HTTPResponse

base_search_url = "https://movie.douban.com/j/search_subjects"

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19042'

d = {
    "type": "tv",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 0
}

url = '{}?{}'.format(base_search_url, urlencode(d))

# urllib3的连接池的管理运营
with urllib3.PoolManager() as http_connect:
    response = http_connect.request('GET', url, headers={
        'User-agent': ua
    })
    print(type(response))
    response: HTTPResponse = HTTPResponse()
    print(response.status)
    print(response.data)
