import requests
import hashlib
import time
import random
import json
URL='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    #'Content-Length':'232',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #'Cookie':'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=1852485387@123.58.182.244; JSESSIONID=abcLCM3I5jfTy_P-El2uw; OUTFOX_SEARCH_USER_ID_NCOO=542927723.7204505; ___rl__test__cookies=1534215287110',
    'Host':'fanyi.youdao.com',
    'Origin':'http://fanyi.youdao.com',
    'Referer':'http://fanyi.youdao.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

def translate(english):
    client = 'fanyideskweb'
    salt = str(int(time.time()*1000)+random.randint(1,10))
    k = 'aNPG!!u6sesA>hBAW1@(-'
    sign = hashlib.md5((client + english + salt + k).encode('utf-8')).hexdigest()
    data={
        'i':english,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false',
    }
    s=requests.post(URL,data=data,headers=headers)
    #print(s.encoding)
    result=json.loads(s.text)
    #print('翻译语言模式:'+result['type'])
    print('\033[1;34m' + '翻译结果为:'+ '\033[0m'+result['translateResult'][0][0]['tgt']+'\n')
def main():
    while True:
        english = input('\033[5;34m' + '输入翻译内容("s"结束翻译)：' + '\033[0m')
        if english=='s':
            print('\033[5;31m' + '翻译结束！'+ '\033[0m')
            break
        else:
            translate(english)

if __name__=='__main__':
    main()
