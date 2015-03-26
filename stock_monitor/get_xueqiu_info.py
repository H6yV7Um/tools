#!/usr/bin/env python
import sys
import time
import sys
import requests
import time
#from sms import sms
import copy
#import mail

#Browser
reload(sys)
sys.setdefaultencoding('utf-8')
def current():
	return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))

def log(content):
	logfile = open('log.txt','a')
	print content
	logfile.write(content + '\n')
	logfile.close()

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
		print url
		print self.cookies
		fetchRes = self.requests.get(url, cookies = self.cookies , headers = self.headers)
		#self.cookies = fetchRes.cookies
		print fetchRes.json()
		if fetchRes.status_code == 200:
			log(current() + ':xueqiu fetch success')
			return fetchRes.json()
		else:
			log(current() + ':xueqiu fetch faild')
			return None

class Shuiniu:
	def __init__(self):
		self.loginUrl = 'https://www.dkhs.com/api/v1/accounts/login/'
		self.fetchUrl = 'https://www.dkhs.com/api/v1/portfolio/91/adjust_positions/'
		self.loginPostData = {
				'email': '547010823@qq.com',
				'is_remember': 'false',
				'password': '60buaichiyu'
				}
		self.requests = requests
		self.cookies = {}
		self.csrftoken = ''

	def login(self):
		loginRes = self.requests.post(self.loginUrl, self.loginPostData)
		self.cookies = loginRes.cookies
		self.csrftoken = loginRes.cookies['csrftoken']
		log(current() + ':shuiniu login success')
		return loginRes.status_code
		#print self.loginRes.json()

	def adjust(self, symbol, percent):
		#,{"symbol":' +  self.symbol2id(toSymbol) + ',"percent":35}
		#'csrfmiddlewaretoken': self.csrftoken
		fetchPostData = {
						'symbols': '[{"symbol":' +  self.symbol2id(symbol) + ',"percent":'+ str(percent) + '}]',
						'csrfmiddlewaretoken': self.csrftoken
						}
		headers = {
					'Referer': self.fetchUrl
		}
		fetchRes = self.requests.post(self.fetchUrl, data = fetchPostData, cookies = self.cookies, headers = headers)
		if fetchRes.status_code == 200:
			log(current() + ':' + symbol + ' to ' + str(percent) + 'success!')
			return True
		else:
			log(current() + ':' + symbol + ' to ' + str(percent) + 'faild!')
			return False
			
	def symbol2id(self, symbol):
		searchUrl = 'https://www.dkhs.com/api/v1/symbols/search/?q='
		res = self.requests.get(searchUrl + symbol)
		if res.status_code == 200:
			return str(res.json()[0]['id'])
		else:
			return None
	#http://121.41.25.170:8010/api/v1/symbols/search/?q=SH000001	
		#print resJson['rebalancing_histories']

#files=(('symbol', '[{"symbol": 101000002,"percent":45},{"symbol": 101000003,"percent":35}]')

#http://121.41.25.170:8010/api/v1/symbols/search/?q=SH000001

def sendMsg(content):
	print 123
	#mail.send_mail(u'xueqiu adjust', content)
	

if __name__ == '__main__':
	xueqiu = Xueqiu()
	xqLoginRes = xueqiu.login()
	#xueqiu.symbol2id('SH000001')
	#xueqiu.adjust('SH601318', 100)
	lastHis = []
	while True:
		try:
			resJson = xueqiu.fetch('http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH003694&count=1&page=1')
		except:
			pass
		print ',,,,,,,,,,,,',resJson

		if resJson:
			histories = resJson[u'list'][0]['rebalancing_histories']
			#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(histories[0]['updated_at'])))
			#update_at = float(histories[0]['updated_at'])
			'''
			sn1 = histories[0]['stock_name'].decode('utf-8')
			ss1 = histories[0]['stock_symbol']
			sw1 =  histories[0]['weight']
			sn2 =  histories[1]['stock_name'].decode('utf-8')
			ss2 = histories[1]['stock_symbol']
			sw2 = histories[1]['weight']
			status = sn1 + '(' + ss1 + ')' + ' ' + str(sw1) + ' to ' + sn2 + '(' + ss2 + ')' + ' ' + str(sw2)
			log(status)
			'''
			if lastHis != histories:
				shuiniu = Shuiniu()
				log('xueqiu change')
				if shuiniu.login() == 200:
					for his in histories:
						log(his['stock_name'].decode('utf-8') + '|' + his['stock_symbol'] + '   adjust to   '+ str(his['weight']))
						sendMsg(his['stock_name'].decode('utf-8') + '|' + his['stock_symbol'] + '    adjust to   '+ str(his['weight']))
						if shuiniu.adjust(his['stock_symbol'], int(his['weight'])):
							log('shuiniu adjust success')
						else:
							log('shuiniu adjust faild')
				else:
					sendMsg('adjust faild!')	
					log('adjust faild')
				lastHis = copy.deepcopy(histories)
			
		else:
			status_code = xueqiu.login()
			if status_code == 200:
				log(current() + ':xueqiu login success')
			else:
				log(current() + ':xueqiu login faild')

		time.sleep(60*4)

