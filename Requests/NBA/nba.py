# -*- coding: utf-8 -*-
import requests
from threading import Timer
from wxpy import *
import datetime
import time

def get_datas():
    url='https://china.nba.com/static/data/scores/miniscoreboard.json'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'
    }
    game_result=requests.get(url,headers=headers).json()['payload']['today']['games']
    game_data = []
    for data in game_result:
        hometeam = data['homeTeam']['profile']['name']
        awayteam = data['awayTeam']['profile']['name']
        awayscore = data['boxscore']['awayScore']
        homescore = data['boxscore']['homeScore']
        isend = data['boxscore']['statusDesc']
        game_data.append(hometeam+'-'+awayteam+':'+str(homescore)+'-'+str(awayscore)+'   '+isend+'\n')
    return ''.join(game_data)
def login_wx():
    try:
        #获取当前时间
        local_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:30', '%Y-%m-%d%H:%M')
        end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '12:30', '%Y-%m-%d%H:%M')
        # 当前时间
        now_time = datetime.datetime.now()
        # 判断当前时间是否在范围时间内
        if now_time > start_time and now_time < end_time:
            datas = get_datas()
            bot.file_helper.send('现在时间是：' + local_time + '\n' + datas)
            t1 = Timer(10, login_wx)
            t1.start()
        else:
            t2 = Timer(86400, login_wx)
            t2.start()
    except:

        bot.file_helper.send(u'数据接收失败')

if __name__ == '__main__':
    #windows下使用
    bot = Bot()
    #Linux下使用
    #bot = Bot(console_qr=2,cache_path=True)
    login_wx()

