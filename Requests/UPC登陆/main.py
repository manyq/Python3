# -*- coding: utf-8 -*-
import socket
from requests import post
from psutil import net_if_addrs

def get_MAC():
    MAC = []
    for k, v in net_if_addrs().items():
        for item in v:
            address = item[1]
            if '-' in address and len(address)==17:
                MAC.append(address)
    return MAC[-1]
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def login(local_ip,MAC):
    url='http://wlan.upc.edu.cn/eportal/InterFace.do?method=login'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data={
        'userId': 1607010320,
        'password': 'myq055060',
        'service': 'cmcc',
        'queryString': 'wlanuserip%3D{}%26wlanacname%3D%26nasip%3D172.22.242.22%26wlanparameter%3D{}%26url%3Dhttp%3A%2F%2Fwww.msftconnecttest.com%2Fredirect%26userlocation%3Dethtrunk%2F62%3A2911.0'.format(local_ip,MAC.lower()),
        'operatorPwd':'',
        'operatorUserId':'',
        'validcode':'',
        'passwordEncrypt':'false',
    }
    r=post(url,data=data,headers=headers)
    if r.status_code==200:
         print("已登陆UPC")

if __name__=='__main__':
    ip=get_host_ip()
    mac=get_MAC()
    login(ip,mac)







