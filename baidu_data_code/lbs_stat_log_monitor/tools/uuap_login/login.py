#!/usr/bin/env python
# -*- coding: utf-8 -*-

 

import urllib2

import urllib

import cookielib

import re

import os

 

 

__cookies__ = os.path.join(os.path.dirname(__file__), 'cookies.txt')

 

class Noah(object):

    def __init__(self, username=None, password=None, logger=None):

 

        self.username = username

        self.password = password

        # self.log = logger

 

        cj = cookielib.FileCookieJar(__cookies__)

        cp = urllib2.HTTPCookieProcessor(cj)

        opener = urllib2.build_opener(cp)

        opener.addheaders = [

            ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.24 ' \

             '(KHTML, like Gecko) Chrome/19.0.1056.0 Safari/535.24'),

            ]

        self._cookiejar = cj

        self._opener = opener

        self.urlopen = self._opener.open

 

    def login(self, username, password):

        resp = self.urlopen('https://uuap.baidu.com/login')

        data = resp.read()

        action = re.findall(r'action="(/login;jsessionid[^"]*)"', data)[0]

        nexturl = 'https://uuap.baidu.com' + action

        lt = re.findall(r'name="lt"\s+value="([^"]*)"', data)[0]

        execution = re.findall(r'name="execution"\s+value="([^"]*)"', data)[0]

        #print line

        data = dict(username=username, password=password,

                    _rememberMe='on', _viaToken='on',

                    lt=lt, execution=execution,

                    _eventId='submit')

        req = urllib2.Request(nexturl, data=urllib.urlencode(data))

        resp = self.urlopen(req)

        return 'Log In Successful' in resp.read()

 

 

def test():

    noah = Noah()

    if not noah.login('zhuangqunxiong', 'goodluck133!'):

        raise SystemExit('Login Failed!')

    # 必须访问, 冲Cookie

    #noah.urlopen('http://noah.baidu.com/olive/index.php?r=Passport/Logging/Index').read()
    #print noah.urlopen('http://noah.baidu.com/ldm_cli/index.php?r=Log/Download/LogView&id=4401').read()
    print noah.urlopen('http://noah.baidu.com/olive/index.php?r=Passport/Logging/Index').read()
    #print noah.urlopen('http://noah.baidu.com/noah/index.php?r=Home/Index').read()
    #print noah.urlopen('http://noah.baidu.com/ldm_cli/index.php?r=Log/Download/LogView&id=5557').read()
    print noah.urlopen('http://noah.baidu.com/ldm_cli/index.php?r=Log/Download/LogView&id=3858').read()

 

 

if __name__ == '__main__':

    test()
