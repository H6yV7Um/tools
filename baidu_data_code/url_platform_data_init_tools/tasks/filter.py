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


def appid2uid(db,line,table,op_date):
    '''self.db.execute_rowcount("insert into clnd_android_app(uid_appid,uid,appid) values(%s,%s,%s)",items[0]+"_"+items[1],items[1],items[0])'''
    line = line.strip()
    if line:
        print line
        tmp = line.split("\t")
        select_value = {"uid_appid":tmp[0]+"_"+tmp[1]}
        insert_value = {"uid":tmp[1],"appid":tmp[0]}
        if db.select(select_value,table) == None:
            db.insert(select_value,insert_value,table)
        else:
            db.update(select_value,insert_value,table)

    pass

'''
chunlei_netdisk_imei    1       1399K   580917210030568

'''
def imei2channel(db,line,table,op_date):
    line = line.strip()
    if line:
        print line
        tmp = line.split("\t")
        if len(tmp) < 4:
            return False
        select_value = {"imei":tmp[3]}
        insert_value = {"clienttype":tmp[1],"origin_channel":tmp[2],"last_channel":tmp[2]}
        update_value = {"clienttype":tmp[1],"last_channel":tmp[2]}
        try:
            if db.select(select_value,table) == None:
                db.insert(select_value,insert_value,table)
            else:
                db.update(select_value,update_value,table)
        except:
            return False

'''
+-----------------+------------------+------+-----+---------------------+----------------+
| Field           | Type             | Null | Key | Default             | Extra          |
+-----------------+------------------+------+-----+---------------------+----------------+
| id              | int(10) unsigned | NO   | PRI | NULL                | auto_increment |
| imei            | varchar(50)      | NO   | UNI | NULL                |                |
| clienttype      | tinyint(1)       | NO   |     | NULL                |                |
| origin_channel  | varchar(30)      | NO   |     | NULL                |                |
| last_channel    | varchar(30)      | YES  |     | NULL                |                |
| create_time     | timestamp        | NO   |     | CURRENT_TIMESTAMP   |                |
| update_time     | timestamp        | NO   |     | 0000-00-00 00:00:00 |                |
| android_version | varchar(100)     | YES  |     | NULL                |                |
| cellphone_type  | varchar(100)     | YES  |     | NULL                |                |
| category        | varchar(50)      | YES  |     | NULL                |                |
+-----------------+------------------+------+-----+---------------------+----------------+


'''


def new_imei(db,line,table,op_date):
    '''1       IPHONE OS_5.0.1_IPHONE 4_CHUNLEI_1415B_WIFI     55952b74e11705b3c4c9693663b9cb20        09-18 00:00:03:'''
    import re
    tmp = line.strip().split("\t")
    imei_re = re.compile("[0-9a-zA-Z]*$")
    valid_list = []
    if len(tmp) >= 3 and imei_re.match(tmp[2]) :
        channel = tmp[1].strip().split("_")
        if len(channel) >= 5 and imei_re.match(channel[4]):
            '''clienttype channel devid category os_version machine_type  '''
            valid_list = [tmp[0],channel[4],tmp[2],channel[0],channel[1],channel[2]]
    print line,valid_list
    if valid_list:
        select_value={"imei":valid_list[2]}
        ret = db.select(select_value,table)
        if not ret:
            insert_value={
            "clienttype":valid_list[0],
            "origin_channel":valid_list[1],
            "last_channel":valid_list[1],
            "category":valid_list[3],
            "android_version":valid_list[4],
            "cellphone_type":valid_list[5],
            "create_time":op_date,
            "update_time":op_date
            }
            try:
                print db.insert(select_value,insert_value,table)
            except:
                return False
        else:
            update_time = ret["update_time"]
            #op_date="20130910"
            check_day = dt.strtodatetime(op_date,"%Y%m%d")
            #check_day = dt.strtodatetime("20130910","%Y%m%d")
            away=dt.datediffbydatetime(update_time,check_day)
            if away.total_seconds() > dt.timedelta(180).total_seconds():
            #if True:
                update_value={
                "last_channel":valid_list[1],
                "category":valid_list[3],
                "android_version":valid_list[4],
                "cellphone_type":valid_list[5],
                "update_time":op_date
                }
                try:
                    print db.update(select_value,update_value,table)
                except:
                    return False
    return True



def netdisk_all_client(db,line,table,op_date):
    import re
    tmp = line.strip().split("\t")
    uid_re = re.compile("[0-9]*$")
    valid_list = []
    if len(tmp) >= 3 and uid_re.match(tmp[2]) :
        '''channel = tmp[1].strip().split("_")
        if len(channel) >= 5 and imei_re.match(channel[4]):
#clienttype channel devid category os_version machine_type
            valid_list = [tmp[0],channel[4],tmp[2],channel[0],channel[1],channel[2]]'''
        category = '0'
        if tmp[1].lower().startswith('android'):
            category = '1'
        else:
            if tmp[1].lower().startswith('iphone'):
                category = '2'
        valid_list = [tmp[2],tmp[0],category]
#print '****',line,valid_list
    if valid_list:
        select_value={}
        '''ret = db.select(select_value,table)
        if not ret:
            insert_value={
            "clienttype":valid_list[0],
            "origin_channel":valid_list[1],
            "last_channel":valid_list[1],
            "category":valid_list[3],
            "android_version":valid_list[4],
            "cellphone_type":valid_list[5],
            "create_time":op_date,
            "update_time":op_date
            }
            try:
                print db.insert(select_value,insert_value,table)
            except:
                return False
        else:
            update_time = ret["update_time"]
            #op_date="20130910"
            check_day = dt.strtodatetime(op_date,"%Y%m%d")
            #check_day = dt.strtodatetime("20130910","%Y%m%d")
            away=dt.datediffbydatetime(update_time,check_day)
            if away.total_seconds() > dt.timedelta(180).total_seconds():
            #if True:
                update_value={
                "last_channel":valid_list[1],
                "category":valid_list[3],
                "android_version":valid_list[4],
                "cellphone_type":valid_list[5],
                "update_time":op_date
                }
                try:
                    print db.update(select_value,update_value,table)
                except:
                    return False'''
        insert_value = {
            "uid":valid_list[0],
            "clienttype":valid_list[1],
            "category":valid_list[2],
            "create_time":op_date,
            "last_time":op_date
        }
        try:
            db.insert(select_value,insert_value,table)
        except:
            return False
    return True

def select_and_insert(db,select_dict,table):
	t = db.select(select_dict,table)
	if t:
		return t
	else:
		db.insert(select_dict,{},table)
		t = db.select(select_dict,table)
		return t

def test(db,line,table,op_date):
	select_dict={'module_name':'lighttpd_log'}
	print "Func[test] deal line[%s"%line
	module = db.select(select_dict,'log_module')
	module_id=None
	if module:
		module_id=module['module_id']
	else:
		db.insert({"function_description":'0',"description":"url add","owner":"qunxiong","module_name":"lighttpd_log"},{},'log_module')
		module = db.select(select_dict,'log_module')
		module_id=module['module_id']

	if line and module_id:
		tmp = line.split('\t')
		if len(tmp) < 4:
			print "Func[test] error line[%s"%line
			return

		host=tmp[0][6:]
		path=tmp[1][6:]
		qt=tmp[2][4:]

		select_dict={'`host`':host,'`path`':path,'module_id':module_id}
		s = db.select(select_dict,'url_host_path')
		host_id = None
		if s:
			host_id = s['host_path_id']
		else:
			db.insert(select_dict,{},'url_host_path')
			s = db.select(select_dict,'url_host_path')
			host_id = s['host_path_id']

		action_name = qt
		select_dict={'host_path_id':host_id,'action_name':action_name,'version':'1','`operation`':'1'}
		t=select_and_insert(db,select_dict,'url_action')
		action_id = t['action_id']

		if action_name=='NO_QT':
			# set action_name as action_id
			print "action_name:%s"%action_name
			s_dict={'action_id' : action_id}
			up_dict={'action_name' : action_id}
			t=db.update(s_dict, up_dict, 'url_action')

		# insert qt info	
		if qt != 'NO_QT':
			select_dict={'`key`':'qt','key_description':"",'`operation`':'1','module_id':module_id}
			t=select_and_insert(db,select_dict,'url_keys')
			
			qt_key_id = t['key_id']
			select_dict={'key_id':qt_key_id, '`value`':qt}
			t = select_and_insert(db, select_dict, 'url_values')

			new_value_id = t['value_id']
			select_dict={'key_id':qt_key_id,'action_id':action_id,'value_id':new_value_id}
			t=select_and_insert(db,select_dict,'url_action_keys')

		keys= tmp[3][5:]
		for key in keys.split("&"):
			select_dict={'`key`':key,'key_description':"",'`operation`':'0','module_id':module_id}
			t=select_and_insert(db,select_dict,'url_keys')
			key_id = t['key_id']
			select_dict={'key_id':key_id,'action_id':action_id}
			t=select_and_insert(db,select_dict,'url_action_keys')


def insert_key_value(db,line,table,op_date):
	if line:
		tmp = line.split('\t')
		key_value=tmp[0][0:];
		it_tmp = key_value.split("=")
		if len(it_tmp) < 2:
			print "Func[insert_key_value] error line[%s"%line
			return

		key   = it_tmp[0]
		value = it_tmp[1]
		select_dict={'`key`':key}
		# query table : url_keys
		s = db.select(select_dict,'url_keys')
		key_id    = None
		module_id = None
		if s:
			key_id    = s['key_id']
			mudule_id = s['module_id']
		else:
			print "Func[insert_key_value] key[%s] is not exist"%key
			return

		s_dict={'key_id' : key_id}
		up_dict={'`operation`' : '1'}
		t=db.update(s_dict, up_dict, 'url_keys')

		# query table:url_values
		select_dict={'key_id':key_id, '`value`':value}
		t = select_and_insert(db, select_dict, 'url_values')
		#print t


def fill_metadata_key(db,line,table,op_date):
	if not line:
		return None
	tmp = line.strip().split('\t')
	module_name=tmp[0]
	key = tmp[1]
	select_dict={'module_name':module_name}
	t = select_and_insert(db, select_dict, 'log_module')
	select_dict={'field_name':key,'`default`':'','module_id':t['module_id'],'data_type':'string','item_type':'notice','log_version':0,'is_require':1,'description':'','`rule`':'','`separator`':1,'has_field_value':0}
	print select_and_insert(db, select_dict, 'log_module_field')

