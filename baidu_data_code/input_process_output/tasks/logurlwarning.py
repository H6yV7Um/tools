#!/bin/env python
# -*- coding:utf-8 -*-


import json
import os
import sys
import copy
import commands
import codecs


class LogUrlWarning():
	def init(self,parameter):
		self.detail_list = ["shortmore","baidu","product","module"]
		self.file_values = ["totalinput","totalmoduleerror","totalerror","totalbaiduerror","totalnoise","totalproducterror"]
		self.parameter = parameter
		pass

	def test(self,aa,bb):
		print aa
		print bb
		return 123

	def parse_err_msg(self,data):
		tmp = {}
		for item in data:
			#print item
			if item in self.detail_list:
				tmp[item] = data[item]
				#print data[item]
		ret = json.dumps(tmp)	
		if len(ret) >= 65535:
			ret = "detail is too long,please check original file"
		return ret 
	
	def finish_process(self,conf,writer):
		'''all line process finish'''
		print "all line process finish"


	def line_process(self,conf,writer,line):
		data = self.line_parse(line)
		if not data:
			return False
		error_msg = self.parse_err_msg(data)
		for value in self.file_values:
			if value not in data:
				data[value] = 0;
		writer.output('insert into log_url_warning(module_name,totalinput,totalmoduleerror,totalproducterror,totalbaiduerror,totalerror,totalnoise,error_msg) values(%s,%s,%s,%s,%s,%s,%s,%s)',conf['module_name'],data['totalinput'],data['totalmoduleerror'],data['totalproducterror'],data['totalbaiduerror'],data['totalerror'],data['totalnoise'],error_msg)
		great_than_threhold,threshold,ratio = self.threshold(conf['threshold'],data['totalerror'],data['totalinput'])
		has_error,clean_data = self.white_list(conf['white_list'],data)
		clean_data['ratio']=ratio
		clean_data['threshold']=threshold
		clean_data['module_name']=conf['module_name']
		#print has_error,great_than_threhold
		print self.email(conf['mail_list'],conf['rd_list'],clean_data,conf['module_name'])

	def threshold(self,threshold,error_num,total_num):
		ratio = float(error_num)*100/float(total_num)	
		return ratio >= float(threshold),threshold,ratio

	def white_list(self,white_list,data):
		tmp_data = copy.deepcopy(data)
		tmp_list = white_list.split(",")
		has_error = False
		for item in data:
			if item in self.detail_list:
				for error in data[item]:
					for key in data[item][error]:					
						if key in tmp_list:
							del tmp_data[item][error][key]
							#print key
						if not tmp_data[item][error]:
							del tmp_data[item][error]
							#print error
		#self.print_data(tmp_data)
		for item in tmp_data:
			if item in self.detail_list and tmp_data[item]:
				has_error = True
		return has_error,tmp_data

	def print_data(self,data):
		for item in data:
			if item in self.detail_list:
				for error in data[item]:
					print data[item][error]
	def data2template(self,wdata):
		key_target = {}	
		detail = {}
		for item in wdata:
			if item not in self.detail_list:
				key_target[item] = wdata[item]
		for item in wdata:
			if item in self.detail_list:
				detail[item] = wdata[item]
		return key_target,detail
						
	def email(self,mail_list,rd_list,wdata,module_name):
		status,output = commands.getstatusoutput('date -d-1day "+%Y%m%d"')
		filename = "../data/%s_%s"%(module_name,output)
		(key_target,detail) = self.data2template(wdata)
		f = codecs.open(filename, 'w', "gbk")

		from jinja2 import Environment, FileSystemLoader, FileSystemBytecodeCache
		env = Environment(loader = FileSystemLoader('../template/'),
				bytecode_cache = FileSystemBytecodeCache('../template/', '%s.cache'))
		tmpl_jinja = env.get_template('testjinja2.html')
		template = tmpl_jinja.render(key_target= key_target,detail=detail)
		print >>f,template
		f.close()
		(status,output) = commands.getstatusoutput('cat %s |formail -I "From: lbsstat-tools@baidu.com" -I "To:%s"  -I "MIME-Version:1.0" -I "Content-type:text/html;charset=gb2312" -I "Subject:%s"|/usr/sbin/sendmail  -oi %s'%(filename,mail_list,os.path.basename(self.parameter[2]),mail_list))
		#(status, output) = commands.getstatusoutput('cat %s | mail -s "%s" %s'%(filename,os.path.basename(self.parameter[2]),mail_list))
		print output
		return status

	def line_parse(self,line):
		ret = {}
		if line.startswith("JASON#:"):
			#tmp = line.split("\t")
			json_dict = json.loads(line[7:])
			for item in json_dict:
				ret[item.lower()] = json_dict[item]
			return ret
		return None

