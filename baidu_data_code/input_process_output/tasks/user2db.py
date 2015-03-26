#!/bin/env python
# -*- coding:utf-8 -*-


import json
import os
import sys
import copy
import commands
import codecs
import traceback

import log
from x_date import *
from data2db import Data2Db

class User2Db(Data2Db):
    def init(self,parameter):
        Data2Db.init(self,parameter)
        try:
            self.action_map = {
                "indoor":1,
                "startnvai":2,
                "yawing":3,
                "appenter":4,
                "endnav":5
            }
            self.action= self.action_map.get(self.parameter[7],0)
        except:
            log.error("task:%s parameters error!!! -> parameters:%s",self.__class__.__name__,self.parameters)
            sys.exit(-1)


   
    def finish_process(self,conf,writer):
        '''all line process finish'''
        log.info("task:%s finished!!!",self.__class__.__name__)

    def str2datetime(self,str,format):
        try:
            ret = strtodatetime(str,format)
        except ValueError:
            return False
        return ret

    def line_process(self,conf,writer,line):
        if not line:
            return None
        try:
            line = line.decode("gb2312").strip()
            tmp_list = line.split('\t')
            client_time = self.str2datetime(tmp_list[0],"%Y%m%d")
            if not client_time:
                client_time = self.str2datetime(tmp_list[0],"%Y-%m-%d")
                if not client_time:
                    raise Exception();
            if not client_time or client_time > self.upload_time:
                raise Exception(); 
            imei = tmp_list[1]
        except:
            self.line_not_to_db(line,self.upload_time,0,"split error")
            return 
        #print self.upload_time,self.product,self.os,self.action,client_time,imei
        try:
            table = "offline_users_list"
            insert_value = {"app":self.product,"os":self.os,"action":self.action,"imei":imei,"client_time":datetime2timestamp(client_time),"upload_time":datetime2timestamp(self.upload_time)}
            writer.insert({},insert_value,table)
        except:
            self.line_not_to_db(line,self.upload_time,0,"insert error")
            traceback.print_exc()

    def update_user_statistic(self,writer,app,os,action,update_time,client_times):
        table = "offline_users_statistic"
        insert_value = {'app':app,'os':os,'action':action,'upload_time':update_time}
        writer.output("delete from offline_users_statistic where upload_time=%s and action=%s",update_time,action)
        for client_time in client_times:
            insert_value['client_time'] = client_time
            active_num = writer.query("select count(1) as num from offline_users_list where client_time=%s and action=%s",client_time,action)[0]["num"]
            total = writer.query("select count(distinct(imei)) as num from offline_users_list where client_time<=%s and action=%s and upload_time<=%s ",client_time,action,update_time)[0]["num"]
            insert_value['active_num'] = active_num
            insert_value['total'] = total
            insert_value['new_num'] = 0
            writer.insert({},insert_value,table)

    def finish_process(self,conf,writer):
        '''all line process finish'''
        #print self.product,self.os,self.action,getYesterday()
        try:
            yesterday = getYesterday()
            update_times = getDaysFromTo(self.upload_time.date(),yesterday)
            client_times = [item["client_time"] for item in writer.query("select distinct(client_time) as client_time from offline_users_list where app=%s and os=%s and action=%s",self.product,self.os,self.action)]
            for update_time in update_times:
                self.update_user_statistic(writer,self.product,self.os,self.action,update_time,client_times)
            #caculate new add user num
            for update_time in update_times:
                self.update_new_num(writer,self.product,self.os,self.action,update_time)
        except:
            log.error("update user statistic error!")
            traceback.print_exc()
        return None

    def update_new_num(self,writer,app,os,action,update_time):
        date2total_dict = {}
        newnum_dict = {}
        for item in writer.query("select total,client_time from offline_users_statistic where upload_time=%s and action=%s order by client_time",update_time,action):
            date2total_dict[item['client_time']] = item['total']
        for key in date2total_dict:
            if (key-86400) in date2total_dict:
                newnum_dict[key] = date2total_dict[key] - date2total_dict[key-86400]
            else:
                newnum_dict[key] = date2total_dict[key]
            writer.output("update offline_users_statistic set new_num=%s where client_time=%s and action=%s and upload_time=%s",newnum_dict[key],key,action,update_time)
        #for i in date2total_dict:
        #    print timestamp2datetime(i),date2total_dict[i]
        #for i in newnum_dict:
        #    print timestamp2datetime(i),newnum_dict[i]
        pass

