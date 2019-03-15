import  requests
import re

url='http://www.upc.edu.cn/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
    }
html = requests.get(url,headers=headers)
reg='src="(.*?\.jpg)"'
img=re.compile(reg)
imglist = re.findall(img,html.content.decode('utf-8','ignore'))#当遇到解析字码出现错误时，用ignore忽略
x = 1
for imgurl in imglist:
    img=requests.get(url+imgurl)
    with open('C:\\images\%s.jpg'%x,'wb')as f:    # 设置了要下载的图片资源路径和要命名的名字
        f.write(img.content)
    print('正在下载第%s张图片' %x)
    x+=1


