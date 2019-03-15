# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}

def get_css(text):
    css=etree.HTML(text)
    css_url=css.xpath('/html/head/link[7]/@href')
    if not css_url:
        raise Exception('找不到css文件')
    css_url='https:'+"".join(css_url)
    class_tag=re.findall(r'<b><span class=\"(.*?)\"></span>',text)
    class_tag=[data[0:2]for data in class_tag][0:1]
    return css_url,class_tag
def get_css_and_px_dict(url):
    pass

def get_svg_threshold_and_int_dict(url,tag):
    text=requests.get(url,headers=headers).content.decode('utf-8')
    #print(text)
    svg_url=re.search(r'span\[class\^="%s"].*?background-image: url((.*?));'%tag,text)
    print(svg_url)
    svg_url='http:'+str(svg_url)
    svg_text=requests.get(svg_url,headers=headers).content.decode('utf-8')
    svg_num=etree.HTML(svg_text).xpath('/svg/text')
    print(svg_num)
    return svg_num
    pass

def get_data(url):
    r=requests.get(url,headers=headers).text
    css_url,class_tag=get_css(r)
    class_tag=''.join(class_tag)
    #print(type(class_tag),class_tag)

    # 获取css对应名与像素的映射
    css_and_px_dict = get_css_and_px_dict(css_url)

    # 获取svg的阈值与数字集合的映射
    svg_threshold_and_int_dict = get_svg_threshold_and_int_dict(css_url, class_tag)
    shops=etree.HTML(r).xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/ul/li')
    for shop in shops:
        pass

def main():
    url='http://www.dianping.com/qingdao/ch10/g110'
    get_data(url)

if __name__ == '__main__':
    main()
