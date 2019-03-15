import requests
import re
headers={
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
}
s=requests.Session()
def login():
    # f=s.get('https://accounts.douban.com/login',headers=headers)
    # code=re.findall(r'<img id="captcha_image" src="(.*?)"',f.text)[0]
    # caID=re.findall(r'<input type="hidden" name="captcha-id" value="(.*?)"',f.text)[0]
    # b=s.get(code,headers=headers)
    # with open('code.png','wb')as fn:
    #     fn.write(b.content)
    data={
        'form_email':'17853267581',
        'form_password':'myq055060',
        'login':'登录',
        'redir':'https://www.douban.com',
        'source':'None',
    }
    a=s.post("https://accounts.douban.com/login",data=data,headers=headers)
    print(a.url)
    if '鑫' in a.text:
        print('登陆成功！')
    else:
        print("登陆失败,正在重新登陆")
        login()

# def comment(mid):
#     f=s.get("https://movie.douban.com/subject/27605698/",headers=headers)
#     ck=re.findall(r'<input type="hidden" name="ck" value="(.*?)">',f.text)
#     print(ck )
#     data={
#         'ck': ck,
#         'interest':'wish',
#         'rating':'',
#         'foldcollect':'F',
#         'tags':'',
#         'comment':'想看，推荐一下'
#     }
#     r=s.post("https://movie.douban.com/j/subject/{}/interest".format(mid),data=data,headers=headers)
#     print(r.text)

# def getmoviesId():
#     r=s.get('https://movie.douban.com/ithil_j/activity/movie_annual2017/widget/5',headers=headers)
#     result=r.json()
#     return result['res']['subjects']

login()
# for i in getmoviesId():
#     print("https://movie.douban.com/subject/{}/".format(i['id']))
#     comment(i['id'])

