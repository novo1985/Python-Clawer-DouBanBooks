from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib import parse
import simplejson

# Try POST method on the test website http://httpbin.org
base_url = 'http://httpbin.org/post'

# body
data = parse.urlencode({
    'name': 'leo, @=/&*',
    'age': 38
})

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19042'

req = Request(base_url, headers={
    'User-agent': ua
})

print(data)

with urlopen(req, data=data.encode()) as res:  # POST data not none
    # with open('c:/Users/leoge/Downloads/httpbin.html', 'wb+') as f:
    #     f.write(res.read())
    #     f.flush()
    # print(res.read())
    # print(res.data())
    text = res.read()
    json_str = simplejson.loads(text)
    print(json_str)
