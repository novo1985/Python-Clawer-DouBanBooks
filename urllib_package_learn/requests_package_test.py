import urllib3
from urllib.parse import urlencode
from urllib3.response import HTTPResponse
import requests


base_search_url = "https://movie.douban.com/j/search_subjects"

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19042'

d = {
    "type": "tv",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 0
}

url = '{}?{}'.format(base_search_url, urlencode(d))

# Usage::
#
#       >>> import requests
#       >>> req = requests.request('GET', 'https://httpbin.org/get')
#       >>> req
#       <Response [200]>

response = requests.request('GET', url, headers={
    'User-agent': ua
})

with response:
    print(response.text)
    print(response.status_code)
    print(response.url)
    print(response.request)
    print(response.headers)


# requests using session to manage send/receive html info, we can also directly use session()
urls = [url, 'https://www.baidu.com/s?wd=magedu']

session = requests.Session()

with session:
    for u in urls:
        res = session.get(u, headers={'User-agent': ua})

        with res:
            print(type(res))
            print(res.headers)
            print(res.status_code)
            print(res.url)
            print(res.request.headers)
            print(res.cookies)
            print(res.text[:20])


