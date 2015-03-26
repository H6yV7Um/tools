#!/bin/env python

import sys

root=sys.path[0]
lib=root+"/../lib"
log=root+"/../log"
conf=root+"/../conf"
data=root+"/../data"
tasks=root+"/../tasks"
sys.path.append(lib)
sys.path.append(tasks)


from x_date import Date
dt = Date()

def all_client_user_num(db_dict,op_date):
    db = db_dict["statistic_db"].getDb()
    result = {}

    for row in db.iter("select category,count(1) as num from clnd_imei group by category;"):
        result[row["category"]] = row["num"]
    return result



def app2uid(db_dict,op_date):
    db = db_dict["statistic_db"].getDb()
    result = {}
    for row in db.iter("select appid,count(*) as num from clnd_android_app group by appid"):
        result[row["appid"]] = row["num"]
    result["dup_total_users"] = db.get("select count(distinct(uid)) as num from clnd_android_app;")["num"]
    return result

def channel_day(db_dict,op_date,category):
    db = db_dict["statistic_db"].getDb()
    begin_day = dt.strtodatetime(op_date,"%Y%m%d")
    end_day = begin_day-dt.timedelta(1)
    result = {}

    for row in db.iter("select last_channel,count(*) as num from clnd_imei where update_time <= %s and update_time > %s and category=%s group by last_channel;",begin_day,end_day,category):
        result[row["last_channel"]] = row["num"]
    for row in db.iter("select count(*) as num from clnd_imei where update_time <= %s and update_time > %s and category=%s ;",begin_day,end_day,category):
        result["total"] = row["num"]
    print "day:",result
    return result

def channel_week(db_dict,op_date,category):
    db = db_dict["statistic_db"].getDb()
    begin_day = dt.strtodatetime(op_date,"%Y%m%d")
    end_day = begin_day-(7*dt.timedelta(1))
    result = {}

    for row in db.iter("select origin_channel,count(*) as num from clnd_imei where create_time <= %s and create_time >= %s and category=%s group by origin_channel;",begin_day,end_day,category):
        result[row["origin_channel"]] = row["num"]
    for row in db.iter("select count(*) as num from clnd_imei where create_time <= %s and create_time >= %s and category=%s ;",begin_day,end_day,category):
        result["total"] = row["num"]
    print "week:",result
    return result


def channel_month(db_dict,op_date,category):
    db = db_dict["statistic_db"].getDb()
    begin_day = dt.strtodatetime(op_date,"%Y%m%d")
    end_day = begin_day-(30*dt.timedelta(1))
    result = {}

    for row in db.iter("select origin_channel,count(*) as num from clnd_imei where create_time <= %s and create_time >= %s and category=%s group by origin_channel;",begin_day,end_day,category):
        result[row["origin_channel"]] = row["num"]
    for row in db.iter("select count(*) as num from clnd_imei where create_time <= %s and create_time >= %s and category=%s ;",begin_day,end_day,category):
        result["total"] = row["num"]
    print "month:",result
    return result

def channel_all(db_dict,op_date,category):
    db = db_dict["statistic_db"].getDb()
    result = {}

    for row in db.iter("select last_channel,count(*) as num from clnd_imei where category=%s  group by last_channel;",category):
        result[row["last_channel"]] = row["num"]
    for row in db.iter("select count(*) as num from clnd_imei where category=%s ;",category):
        result["total"] = row["num"]
    print "all:",result
    return result

def android_channel_all(db_dict,op_date):
    return channel_all(db_dict,op_date,"ANDROID")

def android_channel_day(db_dict,op_date):
    return channel_day(db_dict,op_date,"ANDROID")


def android_channel_month(db_dict,op_date):
    return channel_month(db_dict,op_date,"ANDROID")

   
def android_channel_week(db_dict,op_date):
    return channel_week(db_dict,op_date,"ANDROID")


def ipad_channel_all(db_dict,op_date):
    return channel_all(db_dict,op_date,"IPAD")

def ipad_channel_day(db_dict,op_date):
    return channel_day(db_dict,op_date,"IPAD")


def ipad_channel_month(db_dict,op_date):
    return channel_month(db_dict,op_date,"IPAD")

   
def ipad_channel_week(db_dict,op_date):
    return channel_week(db_dict,op_date,"IPAD")


def iphone_os_channel_all(db_dict,op_date):
    return channel_all(db_dict,op_date,"IPHONE OS")

def iphone_os_channel_day(db_dict,op_date):
    return channel_day(db_dict,op_date,"IPHONE OS")


def iphone_os_channel_month(db_dict,op_date):
    return channel_month(db_dict,op_date,"IPHONE OS")

   
def iphone_os_channel_week(db_dict,op_date):
    return channel_week(db_dict,op_date,"IPHONE OS")

def cellphone_version(db_dict,category):
    db = db_dict["statistic_db"].getDb()
    result = {}

    for row in db.iter("select android_version,count(id) as num from clnd_imei where category=%s group by android_version;",category):
        result[row["android_version"]] = row["num"]
    print category,"version:",result
    return result

def cellphone_type(db_dict,category):
    db = db_dict["statistic_db"].getDb()
    result = {}

    for row in db.iter("select cellphone_type,count(id) as num from clnd_imei where category=%s group by cellphone_type;",category):
        result[row["cellphone_type"]] = row["num"]
    for row in db.iter("select count(id) as num from clnd_imei where category=%s;",category):
        result["total"] = row["num"]
    print category,"type:",result
    return result

def android_cellphone_version(db_dict,op_date):
    return cellphone_version(db_dict,"ANDROID")

def android_cellphone_type(db_dict,op_date):
    return cellphone_type(db_dict,"ANDROID")


def ipad_cellphone_version(db_dict,op_date):
    return cellphone_version(db_dict,"IPAD")

def ipad_cellphone_type(db_dict,op_date):
    return cellphone_type(db_dict,"IPAD")


def iphone_os_cellphone_version(db_dict,op_date):
    return cellphone_version(db_dict,"IPHONE OS")

def iphone_os_cellphone_type(db_dict,op_date):
    return cellphone_type(db_dict,"IPHONE OS")

def yi_all_userid(db_dict,op_date):
    db = db_dict["netdisk_online_db"].getDb()
    result = {}

    for row in db.iter("select uid,deviceid from clnd_userinfo;"):
        result[str(row["uid"])] = str(row["deviceid"])
    print result
    return result

#add by xfw on 20121105
def netdisk_all_client_day(db_dict,op_date,key,clienttype,category):
    db = db_dict["statistic_db"].getDb()
    begin_day = dt.strtodatetime(op_date,"%Y%m%d")
    end_day = begin_day-dt.timedelta(1)
    result = {}

    for row in db.iter("select count(*) as num from clnd_all_client where create_time <= %s and create_time > %s and clienttype=%s and category=%s ;",begin_day,end_day,clienttype,category):
        result[key] = row["num"]
    print "day:",result
    return result

def netdisk_all_client_week(db_dict,op_date,key,clienttype,category):
    db = db_dict["statistic_db"].getDb()
    begin_day = dt.strtodatetime(op_date,"%Y%m%d")
    end_day = begin_day-(7*dt.timedelta(1))
    result = {}

    for row in db.iter("select count(*) as num from clnd_all_client where create_time <= %s and create_time >= %s and clienttype=%s and category=%s ;",begin_day,end_day,clienttype,category):
        result[key] = row["num"]
    print "week:",result
    return result


def netdisk_all_client_month(db_dict,op_date,key,clienttype,category):
    db = db_dict["statistic_db"].getDb()
    begin_day = dt.strtodatetime(op_date,"%Y%m%d")
    end_day = begin_day-(30*dt.timedelta(1))
    result = {}

    for row in db.iter("select count(*) as num from clnd_all_client where create_time <= %s and create_time >= %s and clienttype=%s and category=%s ;",begin_day,end_day,clienttype,category):
        result[key] = row["num"]
    print "month:",result
    return result

def netdisk_all_client(db_dict,op_date,key,clienttype,category):
    db = db_dict["statistic_db"].getDb()
    result = {}

    for row in db.iter("select count(*) as num from clnd_all_client where clienttype=%s and category=%s ;",clienttype,category):
        result[key] = row["num"]
    print "all:",result
    return result

def netdisk_all_client_num(db_dict,op_date):
    result = {}
    result.update(android_netdisk_all_client(db_dict,op_date))
    result.update(android_netdisk_all_client_day(db_dict,op_date))
    result.update(android_netdisk_all_client_month(db_dict,op_date))
    result.update(android_netdisk_all_client_week(db_dict,op_date))
    result.update(ipad_netdisk_all_client(db_dict,op_date))
    result.update(ipad_netdisk_all_client_day(db_dict,op_date))
    result.update(ipad_netdisk_all_client_month(db_dict,op_date))
    result.update(ipad_netdisk_all_client_week(db_dict,op_date))
    result.update(iphone_os_netdisk_all_client(db_dict,op_date))
    result.update(iphone_os_netdisk_all_client_day(db_dict,op_date))
    result.update(iphone_os_netdisk_all_client_month(db_dict,op_date))
    result.update(iphone_os_netdisk_all_client_week(db_dict,op_date))
    result.update(web_netdisk_all_client(db_dict,op_date))
    result.update(web_netdisk_all_client_day(db_dict,op_date))
    result.update(web_netdisk_all_client_month(db_dict,op_date))
    result.update(web_netdisk_all_client_week(db_dict,op_date))
    result.update(pc_netdisk_all_client(db_dict,op_date))
    result.update(pc_netdisk_all_client_day(db_dict,op_date))
    result.update(pc_netdisk_all_client_month(db_dict,op_date))
    result.update(pc_netdisk_all_client_week(db_dict,op_date))
    return result

def android_netdisk_all_client(db_dict,op_date):
    return netdisk_all_client(db_dict,op_date,"android_netdisk_all_client","1","1")

def android_netdisk_all_client_day(db_dict,op_date):
    return netdisk_all_client_day(db_dict,op_date,"android_netdisk_all_client_day","1","1")


def android_netdisk_all_client_month(db_dict,op_date):
    return netdisk_all_client_month(db_dict,op_date,"android_netdisk_all_client_month","1","1")

   
def android_netdisk_all_client_week(db_dict,op_date):
    return netdisk_all_client_week(db_dict,op_date,"android_netdisk_all_client_week","1","1")


def ipad_netdisk_all_client(db_dict,op_date):
    return netdisk_all_client(db_dict,op_date,"ipad_netdisk_all_client","2","0")

def ipad_netdisk_all_client_day(db_dict,op_date):
    return netdisk_all_client_day(db_dict,op_date,"ipad_netdisk_all_client_day","2","0")


def ipad_netdisk_all_client_month(db_dict,op_date):
    return netdisk_all_client_month(db_dict,op_date,"ipad_netdisk_all_client_month","2","0")

   
def ipad_netdisk_all_client_week(db_dict,op_date):
    return netdisk_all_client_week(db_dict,op_date,"ipad_netdisk_all_client_week","2","0")


def iphone_os_netdisk_all_client(db_dict,op_date):
    return netdisk_all_client(db_dict,op_date,"iphone_os_netdisk_all_client","1","2")

def iphone_os_netdisk_all_client_day(db_dict,op_date):
    return netdisk_all_client_day(db_dict,op_date,"iphone_os_netdisk_all_client_day","1","2")


def iphone_os_netdisk_all_client_month(db_dict,op_date):
    return netdisk_all_client_month(db_dict,op_date,"iphone_os_netdisk_all_client_month","1","2")

   
def iphone_os_netdisk_all_client_week(db_dict,op_date):
    return netdisk_all_client_week(db_dict,op_date,"iphone_os_netdisk_all_client_week","1","2")


def web_netdisk_all_client(db_dict,op_date):
    return netdisk_all_client(db_dict,op_date,"web_netdisk_all_client","0","0")

def web_netdisk_all_client_day(db_dict,op_date):
    return netdisk_all_client_day(db_dict,op_date,"web_netdisk_all_client_day","0","0")


def web_netdisk_all_client_month(db_dict,op_date):
    return netdisk_all_client_month(db_dict,op_date,"web_netdisk_all_client_month","0","0")

   
def web_netdisk_all_client_week(db_dict,op_date):
    return netdisk_all_client_week(db_dict,op_date,"web_netdisk_all_client_week","0","0")


def pc_netdisk_all_client(db_dict,op_date):
    return netdisk_all_client(db_dict,op_date,"pc_netdisk_all_client","3","0")

def pc_netdisk_all_client_day(db_dict,op_date):
    return netdisk_all_client_day(db_dict,op_date,"pc_netdisk_all_client_day","3","0")


def pc_netdisk_all_client_month(db_dict,op_date):
    return netdisk_all_client_month(db_dict,op_date,"pc_netdisk_all_client_month","3","0")

   
def pc_netdisk_all_client_week(db_dict,op_date):
    return netdisk_all_client_week(db_dict,op_date,"pc_netdisk_all_client_week","3","0")
