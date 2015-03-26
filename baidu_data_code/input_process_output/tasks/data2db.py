#!/bin/env python
# -*- coding:utf-8 -*-


import json
import os
import sys
import copy
import commands
import codecs
import traceback
import re

import log
from x_date import *

class Data2Db():
    def init(self,parameter):
        self.parameter = parameter
        self.sv_pattern = re.compile(r'([0-9]\.){1,}[0-9]')
        try:
            self.upload_time = strtodatetime(os.path.basename(self.parameter[2]).split(".")[1],"%Y%m%d")
            self.product_map = {
                "map":1,
                "navi":2,
                "sdk":3
            }
            self.os_map = {
                "android":1,
                "iphone":2,
                "ipad":3,
                "wp7":4,
                "wp8":5
            }
            self.product = self.product_map.get(self.parameter[5],0)
            self.os=self.os_map.get(self.parameter[6],0)
        except:
            log.error("task:%s parameters error!!! -> parameters:%s",self.__class__.__name__,self.parameters)
            sys.exit(-1)

    def test(self,aa,bb):
        print aa
        print bb
        return 123

   
    def finish_process(self,conf,writer):
        '''all line process finish'''
        log.info("task:%s finished!!!",self.__class__.__name__)

    def line_not_to_db(self,line,upload_time,client_time,error):
        #print type(line)
        #print line.encode("gbk")
        #log.error(u"line don't enter db upload_time:%s client_time:%s ;%s",upload_time,client_time,line.encode("gbk"))    
        try:
            log.print_log(line.encode("gb2312",'ignore'))
            log.error(error)
        except:
            #print line
            #log.error("miss")
            return

    def filter(self,line,key_en,sv):
        if key_en.startswith(u"contentsnull"):
            self.line_not_to_db(line,self.upload_time,0,"contentsnull error")
            return True
        if not self.sv_pattern.match(sv):
            self.line_not_to_db(line,self.upload_time,0,"sv match error")
            return True
        return False
        pass

    def line_process(self,conf,writer,line):
        if not line:
            return None
        try:
            line = line.decode("gb2312").strip()
            tmp_list = line.split('\t')
            client_time = strtodatetime(tmp_list[0],"%Y-%m-%d")
            if not client_time or client_time > self.upload_time or client_time < strtodatetime("201208","%Y%m"):
                raise Exception()
            key_en = tmp_list[1]
            num = int(tmp_list[2])
            sv = tmp_list[-1]
            if self.filter(line,key_en,sv):
                return
        except:
            self.line_not_to_db(line,self.upload_time,0,"split error")
            return 
        try:
            select_value = {"app":self.product,"os":self.os,"sv":sv,"key_en":key_en}
            ret  = writer.select_and_insert(select_value,"offline_key_map")
        except:
            self.line_not_to_db(line,self.upload_time,0,"select_and_insert error")
            return 
        if not ret:
            self.line_not_to_db(line,self.upload_time,0,"select_and_insert error")
            return 
       #print ret['id'],datetime2timestamp(self.upload_time),datetime2timestamp(client_time),num
        try:
            table = "offline_button_count_"+client_time.strftime("%Y%m")
            insert_value = {"id":ret['id'],"num":num,"client_time":datetime2timestamp(client_time),"upload_time":datetime2timestamp(self.upload_time)}
            writer.insert({},insert_value,table)
        except:
            self.line_not_to_db(line,self.upload_time,0,"insert error")
            traceback.print_exc()
        pass

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

