import requests
r = requests.get("http://httpbin.org/ip")
print(r.text)

r = requests.get("http://httpbin.org/get?name='akui'&email='a_kui@163.con'")
print(r.text)
print(r.json())
print(r.status_code)
print(r.headers)
print(r.cookies)
