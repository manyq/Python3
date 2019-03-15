import requests
import re
from PIL import Image
import urllib.request
from bs4 import BeautifulSoup

url='http://jwxt.upc.edu.cn'
headers = {
        # 'Host':'jwxt.upc.edu.cn',
        # 'Origin':'http://jwxt.upc.edu.cn',
        # 'Referer':'http://jwxt.upc.edu.cn/jwxt/',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)'
}

s=requests.Session()
f=s.get('http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logon',headers=headers)
#print(f.text)

randomcode=(re.findall(re.compile('src="(.*?\.servlet)"'),f.text))[0]

#读取验证码：
b=s.get(url+randomcode,headers=headers)
with open('code.jpg','wb') as f:
     f.write(b.content)
data = {
       'USERNAME':input('请输入学号:'),
       'PASSWORD':input('请输入密码:'),
       'useDogCode':'',
       'useDogCode':'',
       'RANDOMCODE':input('请输入验证码:')
}

a=s.post('http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logon',data=data,headers=headers)
#print(a.url)
m=s.get('http://jwxt.upc.edu.cn/jwxt/framework/main.jsp',headers=headers)
print(m.content.decode('utf-8'))
