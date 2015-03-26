#!/usr/bin/env python
#  -*- coding:utf8 -*-
import sys
import time
import requests
import time
#from sms import sms
import datetime
import json

#from sendmail import SINGAL_MAIL
from sendmail import Mails
#import mail

#Browser
reload(sys)
sys.setdefaultencoding('utf-8')
def current():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))

def log(content):
    logfile = open('log.txt','a')
    logfile.write(content + '\n')
    logfile.close()



def need_curl():
    hour = datetime.datetime.now().hour
    return hour > 8 and hour < 15


class Xueqiu:
    def __init__(self):
        self.loginUrl = 'http://xueqiu.com/user/login'
        self.loginPostData = {
                'username':'',
                'areacode':'86',
                'telephone':'18030200310',
                'remember_me':'0',
                'password':'EF6D0FE0B1833BA7C9D13E23E5D8A4B9'
                }
        self.requests = requests
        self.cookies = {}
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
                'Host': 'xueqiu.com',
                'Pragma': 'no-cache',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Cache-Conrol': 'no-cache',
                'Referer': 'http://xueqiu.com/P/ZH003694',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Language': 'zh-CN,zh;q=0.8'
                }
    def pre_fetch(self):
        fetchRes = self.requests.get('http://www.xueqiu.com/', cookies = self.cookies, headers = self.headers)
        return fetchRes.status_code

    def login(self):
        self.pre_fetch()
        loginRes = self.requests.post(self.loginUrl, cookies = self.cookies, data = self.loginPostData, headers = self.headers)
        self.cookies = loginRes.cookies
        
        return loginRes.status_code
        #print loginRes.json()


    def fetch(self, url):
        if not need_curl():
            return None
        print url
        fetchRes = self.requests.get(url, cookies = self.cookies , headers = self.headers)
        #self.cookies = fetchRes.cookies
        #print fetchRes.json()
        if fetchRes.status_code == 200:
            log(current() + ':xueqiu fetch success')
            return fetchRes.json()
        else:
            log(current() + ':xueqiu fetch faild')
            return None


def need_send(created_at):
    created_at = created_at/1000
    now=int(time.time())
    #cd = datetime.datetime.fromtimestamp(created_at).strftime('%Y-%m-%d %H:%M:%S')
    #nd = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
    cd = datetime.datetime.fromtimestamp(created_at)
    nd = datetime.datetime.fromtimestamp(now)
    #return True
    return nd-cd < datetime.timedelta(minutes=3)


def send_details(resJson,combination_name="最新"):
    if not resJson:
        log(current() + ': %s is None'%combination_name)
        return 
    if 'list' in resJson:
        lastest = resJson['list'][0]
        created_at = lastest.get('created_at', None)
        if not need_send(created_at):
            return 
        change_info = ""
        for rebalancing_history in lastest['rebalancing_histories']:
            change_info += "%s\t%s\t\t%s==>%s\n"%(rebalancing_history.get('stock_name', None),rebalancing_history.get('stock_symbol', None),rebalancing_history.get('prev_weight', None),rebalancing_history.get('target_weight', None))
        a=Mails("smtp.163.com", "25", "username", "passwd")
        #print type(change_info.encode("utf8", "ignore"))
        a.send("%s调仓更新 %s"%(combination_name, datetime.datetime.fromtimestamp(created_at/1000)), change_info.encode("utf8", "ignore"), "qxiong133@163.com", ["zqx2010@gmail.com","348297509@qq.com","Zengshengdi@qq.com","15960395077@163.com","258565043@qq.com",])
        #a.send("%s调仓更新 %s"%(combination_name, datetime.datetime.fromtimestamp(created_at/1000)), change_info.encode("utf8", "ignore"), "qxiong133@163.com", ["zqx2010@gmail.com","348297509@qq.com","258565043@qq.com",])

    

if __name__ == '__main__':
    xueqiu = Xueqiu()
    xqLoginRes = xueqiu.login()
    while True:
        try:
            resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH003694&count=1&page=1')
            send_details(resJson,"东坡1号")
            resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH010389&count=1&page=1')
            send_details(resJson,"誓把老刀挑下位")
            resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH002820&count=1&page=1')
            send_details(resJson,"天下第一输")
            resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH027696&count=1&page=1')
            send_details(resJson,"牛市谁最牛")
            resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH016352&count=1&page=1')
            send_details(resJson,"飞猫")
            resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH233863&count=1&page=1')
            send_details(resJson,"测试组合")
        except:
            print sys.exc_info()
            pass
        time.sleep(60*3)

