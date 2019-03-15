import requests
import re
import execjs
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
}
s = requests.Session()
f = s.get('http://cas.upc.edu.cn/cas/login', headers=headers)

loginErrCnt = re.findall(r'<input type="hidden" name="loginErrCnt" value="(.*?)"', f.text)[0]
lt = re.findall(r'<input type="hidden" name="lt" value="(.*?)"', f.text)[0]

password = input('输入密码:')
passwd = execjs.compile(open(r'md5.js').read()).call('hex_md5', password)
# print(passwd)
data = {
    'encodedService': 'http%3a%2f%2fi.upc.edu.cn',
    'service': 'http://i.upc.edu.cn',
    'serviceName': 'null',
    'loginErrCnt': loginErrCnt,
    'username': '1607010320',
    'password': passwd,
    'lt': lt,
}

s.post('https://cas.upc.edu.cn/cas/login', data=data, headers=headers)

header = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'clientType':'json',
    'Connection':'keep-alive',
    'Content-Length':'83',
    'Content-Type':'text/plain;charset=UTF-8',
    'Host':'i.upc.edu.cn',
    'Origin':'https://i.upc.edu.cn',
    'render':'json',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
}
data = {
    "map":{
        "method":"getSsoDetailInfo",
            "params":""},
        "javaClass":"java.util.HashMap"}

b = s.post('https://i.upc.edu.cn/dcp/sso/sso.action', data=json.dumps(data), headers=header)
print(b)
