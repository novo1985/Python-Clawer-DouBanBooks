import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import simplejson

base_search_url = "https://movie.douban.com/j/search_subjects"

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19042'

dict = {
    "type": "tv",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 0
}

# 拼接url: base + encoded specific conditions '{}?{}'.format() function
req = Request('{}?{}'.format(base_search_url, urlencode(dict)), headers={
    "User-agent": ua
})

with urlopen(req) as res:
    try:
        output_detail = simplejson.loads(res.read())
        print(len(output_detail["subjects"]))
        print(output_detail["subjects"])
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)





