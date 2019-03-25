# -*- coding: utf-8 -*-
#只实现了登陆12306
import requests
from lxml import etree
def captcha(index):#将图片坐标转换为图片序列
    params={
        '1':'35,45',
        '2':'110,45',
        '3':'180,45',
        '4':'250,45',
        '5':'35,115',
        '6':'110,115',
        '7':'180,115',
        '8':'250,115',
    }
    index=index.split(',')
    temp=[]
    for i in index:
        temp.append(params[i])
    return ','.join(temp)
def login():
    captcha_check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
    session=requests.Session()#保持登陆状态
    headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    code=session.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.20547998272022672')
    with open('captcha.jpg','wb')as fn:#下载并打开验证码
        fn.write(code.content)
    formdata={
        'answer':captcha(input('输入验证码的图片序号>>')),#序号之间用逗号分隔
        'login_site':'E',
        'rand':'sjrand',
    }
    captcha_check=session.post(captcha_check_url,data=formdata,headers=headers).json()
    #print(captcha_check)
    if captcha_check['result_code']=='4':
        login_url='https://kyfw.12306.cn/passport/web/login'
        login_data={
            'username':input('输入你的用户名>>'),
            'password':input('输入你的密码>>'),
            'appid':'otn',
        }
        login=session.post(login_url,data=login_data).json()
        #print(login)
        if login['result_code']==0:
            uamtk_url='https://kyfw.12306.cn/passport/web/auth/uamtk'
            uamtk_data={
                'appid':'otn',
            }
            uamtk=session.post(uamtk_url,data=uamtk_data).json()
            #print(uamtk)
            if uamtk['result_code']==0:
                uamauthclient_url='https://kyfw.12306.cn/otn/uamauthclient'
                uamauthclient_data={
                    'tk':uamtk['newapptk']
                }
                uamauthclient=session.post(uamauthclient_url,data=uamauthclient_data).json()
                #print(uamauthclient)
                initMy12306_url='https://kyfw.12306.cn/otn/index/initMy12306'
                initMy12306=session.get(initMy12306_url).text
                print(initMy12306)
    else:
        print(captcha_check['result_message'])
if __name__ == '__main__':
    login()
