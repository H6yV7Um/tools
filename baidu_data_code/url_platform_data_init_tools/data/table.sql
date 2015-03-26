-- MySQL dump 10.11
--
-- Host: 127.0.0.1    Database: metadatapf
-- ------------------------------------------------------
-- Server version	5.0.45-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `log_behavior`
--

DROP TABLE IF EXISTS `log_behavior`;
CREATE TABLE `log_behavior` (
  `behavior_id` int(11) NOT NULL auto_increment,
  `flag` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `module_id` int(11) NOT NULL,
  `behavior_name` varchar(255) NOT NULL,
  PRIMARY KEY  (`behavior_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_behavior`
--

LOCK TABLES `log_behavior` WRITE;
/*!40000 ALTER TABLE `log_behavior` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_behavior` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_behavior_field`
--

DROP TABLE IF EXISTS `log_behavior_field`;
CREATE TABLE `log_behavior_field` (
  `behavior_field_id` int(11) NOT NULL auto_increment,
  `field_id` int(11) NOT NULL,
  `behavior_id` int(11) NOT NULL,
  PRIMARY KEY  (`behavior_field_id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_behavior_field`
--

LOCK TABLES `log_behavior_field` WRITE;
/*!40000 ALTER TABLE `log_behavior_field` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_behavior_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_field`
--

DROP TABLE IF EXISTS `log_field`;
CREATE TABLE `log_field` (
  `field_id` int(11) NOT NULL auto_increment,
  `field_name` varchar(255) NOT NULL,
  `default` varchar(255) NOT NULL,
  `is_product` tinyint(4) NOT NULL COMMENT '是否是产品线必打字段，0是百度必打字段，1是产品线必打字段',
  `data_type` varchar(255) NOT NULL,
  `item_type` varchar(255) NOT NULL,
  `log_version` int(11) NOT NULL,
  `rule` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `has_field_value` int(11) NOT NULL,
  PRIMARY KEY  (`field_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_field`
--

LOCK TABLES `log_field` WRITE;
/*!40000 ALTER TABLE `log_field` DISABLE KEYS */;
INSERT INTO `log_field` VALUES (35,'cuid','',1,'string','',0,'','用户身份的唯一识别。用来取代原来的imei号。 要求：凡是能获取到cuid的地方都打印出来。cuid的组成：deviceid|imei逆序。',0),(36,'imei','',1,'string','',0,'','国际移动设备身份码,手机的唯一标识。今后imei会被cuid取代，但是考虑到统计的平滑过渡，在能获取到imei号的地方依然是必须打出来。',0),(37,'apinfo','',1,'string','',0,'','apinfo=xxx，定位依据。',0),(38,'locxy','',1,'string','',0,'','定位到的坐标, locxy=(x,y,r)',0),(40,'product','',0,'string','',0,'','产品线标示。一个产品线有一个，值的类型为字符串。Product字段在webserver产生，使用”HTTP_X_BD_PRODUCT”字段向后传递。由Lighttpd产生并打印，向后传递',1),(41,'subsys','',0,'string','',0,'','业务/子系统标识，这个字段用户标识一个请求的一个从前到后完整的子系统或者业务。值的类型为字符串，例如贴吧的frs子系统，空间的blog子系统。subsys字段在webserver产生，使用”HTTP_X_BD_SUBSYS”字段向后传递。由Lighttpd产生并打印，向后传递。',0),(42,'module','',0,'string','',0,'','模块标识，一个业务/子系统里通常会有多个模块。如blogui，bloglogic等。',0),(44,'reqip','',1,'string','',0,'/(\\d{1,3}\\.){3}(\\d{1,3})/	','上游调用方ip；',0),(47,'cost','0',1,'int','',0,'/\\d+/','表示请求在本module内的总耗时，单位ms，包括了在本module发生的交互的时间。',0),(48,'optime','0',0,'string','',0,'/\\d+\\.\\d{3}/','打印日志的时间，分别打印出s和ms，格式如下：123456.123 （秒.毫秒）',0),(49,'errno','0',0,'int','',0,'/\\d+/','Warning日志必须有自己的唯一出错标示；',0),(55,'logid','',0,'bigint','',0,'/\\d+/','logid在webserver产生，一个请求对应于一个logid，logid贯穿这个请求在服务器端的整个过程不发生变化。	',0),(56,'baiduid','',0,'string','',0,'','百度用户唯一标识',0),(57,'url','',0,'string','',0,'','访问URL，需要urlencode	',0),(58,'refer','',0,'string','',0,'','访问来源地址，需要urlencode	',0),(61,'host','',0,'string','',0,'','HTTP请求中Host的header，即本次请求的域名	',0),(62,'ua','',0,'string','',0,'','浏览器客户端标识（User-Agent），需要urlencode',0),(63,'local_ip','',0,'string','',0,'/(\\d{1,3}\\.){3}(\\d{1,3})/','当前机器IP',0),(64,'client_ip','',0,'string','',0,'/(\\d{1,3}\\.){3}(\\d{1,3})/','用户IP',0);
/*!40000 ALTER TABLE `log_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_field_value`
--

DROP TABLE IF EXISTS `log_field_value`;
CREATE TABLE `log_field_value` (
  `value_id` int(11) NOT NULL auto_increment,
  `value` varchar(255) NOT NULL,
  `field_id` int(11) NOT NULL,
  `field_domain` int(4) NOT NULL,
  `description` varchar(255) default NULL,
  PRIMARY KEY  (`value_id`)
) ENGINE=InnoDB AUTO_INCREMENT=207 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_field_value`
--

LOCK TABLES `log_field_value` WRITE;
/*!40000 ALTER TABLE `log_field_value` DISABLE KEYS */;
INSERT INTO `log_field_value` VALUES (206,'map',40,0,'地图主站（示例，如果不符请修改）');
/*!40000 ALTER TABLE `log_field_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_module`
--

DROP TABLE IF EXISTS `log_module`;
CREATE TABLE `log_module` (
  `module_id` int(11) NOT NULL auto_increment,
  `description` varchar(255) NOT NULL,
  `owner` varchar(255) NOT NULL,
  `function_description` int(11) NOT NULL,
  `module_name` varchar(255) NOT NULL,
  PRIMARY KEY  (`module_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_module`
--

LOCK TABLES `log_module` WRITE;
/*!40000 ALTER TABLE `log_module` DISABLE KEYS */;
INSERT INTO `log_module` VALUES (13,'map主站前端日志','暨灿',0,'lighttpd_log'),(14,'api前端日志','高峰',0,'api_lighttpd_log'),(15,'主站phpui日志','暨灿',0,'map_phpui'),(16,'api的phpui日志','王靖',0,'map_api_phpui'),(17,'定位后端日志','乔丹',0,'dingwei_loc1(map_dinwei_loccenter_lo)'),(18,'手机断点续传日志','王靖',0,'map_mmproxy_log'),(19,'路况后端日志','宝山',0,'map_its_control'),(21,'wapmap日志','小鹏',0,'wapmaplighttpd'),(22,'手机地图后端服务','李超',0,'mobilemap_log'),(23,'wapmap的phpui','小鹏',0,'wapmap');
/*!40000 ALTER TABLE `log_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_module_field`
--

DROP TABLE IF EXISTS `log_module_field`;
CREATE TABLE `log_module_field` (
  `field_id` int(11) NOT NULL auto_increment,
  `field_name` varchar(255) NOT NULL,
  `default` varchar(255) NOT NULL,
  `module_id` tinyint(4) NOT NULL COMMENT '模块id ',
  `data_type` varchar(255) NOT NULL,
  `item_type` varchar(255) NOT NULL,
  `log_version` int(11) NOT NULL,
  `is_require` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `rule` varchar(255) NOT NULL,
  `separator` varchar(255) NOT NULL,
  `has_field_value` int(11) NOT NULL,
  PRIMARY KEY  (`field_id`)
) ENGINE=InnoDB AUTO_INCREMENT=205 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `log_module_field`
--

LOCK TABLES `log_module_field` WRITE;
/*!40000 ALTER TABLE `log_module_field` DISABLE KEYS */;
INSERT INTO `log_module_field` VALUES (47,'type','',17,'string','notice',0,1,'请求类型','','1',0),(48,'query_string','',23,'string','notice',0,1,'查询串','','',0),(49,'query_type','',23,'string','notice',0,1,'检索类型','','',0),(50,'last_page','',23,'string','notice',0,1,'末次执行页面','','',0),(51,'mem_cost','',23,'int','notice',0,1,'内存消耗','','',0),(53,'ispv','',19,'int','notice',0,1,'是否pv统计标识','','',0),(54,'is_partial','',19,'int','notice',0,1,'是否断点续传标识','','',0),(55,'query','',17,'string','notice',0,1,'请求明文','','',0),(56,'info','',17,'string','notice',0,1,'定位详细信息','','',0),(57,'result','',17,'string','notice',0,1,'定位结果json','','',0),(58,'time_cost','',23,'int','notice',0,1,'时间消耗','','',0),(59,'q_wd','',16,'string','notice',0,1,'检索词','','',0),(60,'q_qt','',16,'string','notice',0,1,'query type','','',0),(61,'q_cc','',16,'int','notice',0,1,'城市百度内部code码','','',0),(62,'q_pn','',16,'int','notice',0,1,'page number','','',0),(63,'q_rn','',16,'int','notice',0,1,'result number','','',0),(64,'q_l','',16,'int','notice',0,1,'地图缩放级别','','',0),(65,'q_b','',16,'string','notice',0,1,'图区范围','','',0),(66,'q_ar','',16,'string','notice',0,1,'手机客户端bound','','',0),(67,'q_uid','',16,'string','notice',0,1,'poiuid','','',0),(68,'q_sn','',16,'int','notice',0,1,'起始点表示','','',0),(69,'q_en','',16,'int','notice',0,1,'终止点表示','','',0),(70,'q_sc','',16,'int','notice',0,1,'起始城市code码','','',0),(71,'q_ec','',16,'int','notice',0,1,'终止城市code码','','',0),(72,'q_suid','',16,'string','notice',0,1,'起始地点uid','','',0),(73,'q_euid','',16,'string','notice',0,1,'终止地点uid','','',0),(74,'q_cwd','',16,'string','notice',0,1,'中心点','','',0),(75,'q_drpt','',16,'string','notice',0,1,'拖拽点坐标，对应老日志pt','','',0),(76,'q_w','',16,'int','notice',0,1,'','','',0),(77,'q_m','',16,'string','notice',0,1,'公交相关参数','','',0),(78,'q_f','',16,'string','notice',0,1,'公交相关参数','','',0),(79,'q_mo','',16,'int','notice',0,1,'统计用参数','','',0),(80,'q_tp','',16,'int','notice',0,1,'检索数据源种类','','',0),(81,'q_srt','',16,'int','notice',0,1,'排序类型','','',0),(82,'q_et','',16,'int','notice',0,1,'','','',0),(83,'q_r','',16,'int','notice',0,1,'周边检索半径','','',0),(84,'q_sy','',16,'int','notice',0,1,'','','',0),(85,'q_gt','',16,'int','notice',0,1,'','','',0),(86,'q_drag','',16,'int','notice',0,1,'','','',0),(87,'q_src','',16,'int','notice',0,1,'','','',0),(88,'q_db','',16,'int','notice',0,1,'','','',0),(89,'q_geocty','',16,'int','notice',0,1,'','','',0),(90,'q_sampling','',16,'string','notice',0,1,'','','',0),(91,'p_type','',16,'int','notice',0,1,'','','',0),(92,'p_cname','',16,'string','notice',0,1,'','','',0),(93,'p_ctype','',16,'int','notice',0,1,'','','',0),(94,'p_cc','',16,'int','notice',0,1,'','','',0),(95,'p_sd','',16,'int','notice',0,1,'','','',0),(96,'p_res_no','',16,'int','notice',0,1,'','','',0),(97,'p_cn','',16,'int','notice',0,1,'','','',0),(98,'p_s_city','',16,'int','notice',0,1,'','','',0),(99,'p_s_res','',16,'int','notice',0,1,'','','',0),(100,'p_e_city','',16,'int','notice',0,1,'','','',0),(101,'p_e_res','',16,'int','notice',0,1,'','','',0),(102,'p_rb','',16,'int','notice',0,1,'','','',0),(103,'p_bc','',16,'int','notice',0,1,'','','',0),(104,'p_ca','',16,'int','notice',0,1,'','','',0),(105,'p_sugq','',16,'int','notice',0,1,'','','',0),(106,'p_specr','',16,'int','notice',0,1,'','','',0),(107,'p_resid','',16,'int','notice',0,1,'','','',0),(108,'p_res','',16,'int','notice',0,1,'','','',0),(109,'p_on_gel','',16,'int','notice',0,1,'','','',0),(110,'p_op_gel','',16,'int','notice',0,1,'','','',0),(111,'p_gr','',16,'int','notice',0,1,'','','',0),(112,'p_tn','',16,'int','notice',0,1,'','','',0),(113,'p_errno','',16,'int','notice',0,1,'','','',0),(114,'p_sr_lc','',16,'int','notice',0,1,'','','',0),(115,'p_place','',16,'int','notice',0,1,'','','',0),(117,'p_d_data_type','',16,'int','notice',0,1,'','','',0),(118,'p_strategy','',16,'int','notice',0,1,'','','',0),(119,'用户ip','',14,'string','notice',0,1,'请求用户的ip，目前是由transmit带一个http的header来标识','','',0),(120,'远程ip','',14,'string','notice',0,1,'lighttpd前端的ip','','',0),(121,'log id','',14,'int','notice',0,1,'现在不支持，全部打印0占位','','',0),(122,'请求日期','',14,'string','notice',0,1,'','','',0),(123,'请求处理时间','',14,'int','notice',0,1,'整数，单位ms','','',0),(124,'请求url','',14,'string','notice',0,1,'','','',0),(125,'range','',19,'string','notice',0,1,'断点续传请求范围（如0-20479）','','',0),(126,'请求host','',14,'string','notice',0,1,'','','',0),(127,'http响应状态码','',14,'int','notice',0,1,'','','',0),(128,'响应字节数','',14,'int','notice',0,1,'','','',0),(129,'gzip压缩比例','',14,'string','notice',0,1,'格式 为: gzip: {xxx}pct。其中{xxx}代表数字，为了兼容','','',0),(130,'referer','',14,'string','notice',0,1,'','','',0),(131,'cookie','',14,'string','notice',0,1,'','','',0),(132,'user-agent','',14,'string','notice',0,1,'','','',0),(133,'product','',14,'string','notice',0,1,'','','',0),(134,'subsys','',14,'string','notice',0,1,'','','',0),(135,'本地ip','',14,'string','notice',0,1,'当前机器ip','','',0),(136,'logtype','',22,'string','notice',0,1,'','/[0-9a-zA-Z]/','',0),(137,'os','',22,'string','notice',0,1,'手机操作系统','/[0-9a-zA-Z,_-.]/','',0),(138,'channel','',22,'string','notice',0,1,'渠道','/[0-9a-zA-Z,_-.]/','',0),(139,'mb','',22,'string','notice',0,1,'机型','/[0-9a-zA-Z,_-.]/','',0),(140,'q.wd','',15,'string','notice',0,1,'检索词','','',0),(141,'q.qt','',15,'string','notice',0,1,'query type','','',0),(142,'q.cc','',15,'int','notice',0,1,'城市百度内部code码','','',0),(143,'q.pn','',15,'int','notice',0,1,'page number','','',0),(144,'q.rn','',15,'int','notice',0,1,'result number','','',0),(145,'q.l','',15,'int','notice',0,1,'地图缩放级别','','',0),(146,'q.b','',15,'string','notice',0,1,'图区范围','','',0),(147,'q.ar','',15,'string','notice',0,1,'','','',0),(148,'q.uid','',15,'string','notice',0,1,'poiuid','','',0),(149,'q.sn','',15,'int','notice',0,1,'起始点表示','','',0),(150,'q.en','',15,'int','notice',0,1,'终止点表示','','',0),(151,'q.sc','',15,'int','notice',0,1,'起始城市code码','','',0),(152,'q.ec','',15,'int','notice',0,1,'终止城市code码','','',0),(153,'q.suid','',15,'string','notice',0,1,'起始地点uid','','',0),(154,'q.euid','',15,'string','notice',0,1,'终止地点uid','','',0),(155,'q.cwd','',15,'string','notice',0,1,'中心点','','',0),(156,'q.drpt','',15,'string','notice',0,1,'拖拽点坐标，对应老日志pt','','',0),(157,'q.w','',15,'int','notice',0,1,'','','',0),(158,'q.m','',15,'string','notice',0,1,'公交相关参数','','',0),(159,'q.f','',15,'string','notice',0,1,'公交相关参数','','',0),(160,'q.mo','',15,'int','notice',0,1,'统计用参数','','',0),(161,'q.tp','',15,'int','notice',0,1,'检索数据源种类','','',0),(162,'q.srt','',15,'int','notice',0,1,'排序类型','','',0),(163,'q.et','',15,'int','notice',0,1,'','','',0),(164,'q.r','',15,'int','notice',0,1,'周边检索半径','','',0),(165,'q.sy','',15,'int','notice',0,1,'公交驾车策略','','',0),(166,'q.gt','',15,'int','notice',0,1,'统计用参数','','',0),(167,'q.drag','',15,'int','notice',0,1,'是否是拖拽','','',0),(168,'q.src','',15,'int','notice',0,1,'检索来源','','',0),(169,'q.db','',15,'int','notice',0,1,'是否debug','','',0),(170,'q.geocty','',15,'int','notice',0,1,'','','',0),(171,'q.from','',15,'string','notice',0,1,'请求来源','','',0),(172,'q.reqflag','',15,'string','notice',0,1,'请求标识','','',0),(173,'p.type','',15,'int','notice',0,1,'返回结果类型','','',0),(174,'p.cname','',15,'string','notice',0,1,'city 检索结果所在城市名','','',0),(175,'p.ctype','',15,'int','notice',0,1,'城市类型，统计用参数','','',0),(176,'p.cc','',15,'int','notice',0,1,'是否更新当前城市，用于统计','','',0),(177,'p.sd','',15,'int','notice',0,1,'是否出“设置默认城市”的连接，用于统计','','',0),(178,'p.res_no','',15,'int','notice',0,1,'','','',0),(179,'p.cn','',15,'int','notice',0,1,'当前城市否是有结果','','',0),(180,'p.s_city','',15,'int','notice',0,1,'起始城市','','',0),(181,'p.s_res','',15,'int','notice',0,1,'起点有无结果','','',0),(182,'p.e_city','',15,'int','notice',0,1,'终点城市','','',0),(183,'p.e_res','',15,'int','notice',0,1,'终点有无结果','','',0),(184,'p.rb','',15,'int','notice',0,1,'公交/驾车地址选择页是否起始点都有结果','','',0),(185,'p.bc','',15,'int','notice',0,1,'驾车和步行路线是否在同一个城市','','',0),(186,'p.ca','',15,'int','notice',0,1,'是否出天气预报','','',0),(187,'p.sugq','',15,'int','notice',0,1,'是否有sugq','','',0),(188,'p.specr','',15,'int','notice',0,1,'是否有省道/国道','','',0),(189,'p.resid','',15,'int','notice',0,1,'无线发来的统计','','',0),(190,'p.res','',15,'int','notice',0,1,'Open-api统计用参数','','',0),(191,'p.on_gel','',15,'int','notice',0,1,'指定as出泛需求结果标识','','',0),(192,'p.op_gel','',15,'int','notice',0,1,'as返回泛需求结果标识','','',0),(193,'p.gr','',15,'int','notice',0,1,'Fe发送统计用参数','','',0),(194,'p.tn','',15,'int','notice',0,1,'控制用参数，用来控制是否输出hotcity 天气 以及specail data','','',0),(195,'p.errno','',15,'int','notice',0,1,'','','',0),(196,'p.sr_lc','',15,'int','notice',0,1,'','','',0),(197,'p.place','',15,'int','notice',0,1,'place行业类型统计参数','','',0),(198,'p.place_ex','',15,'int','notice',0,1,'place行业类型统计参数','','',0),(199,'p.place_sort','',15,'int','notice',0,1,'place数据d_sort_type统计参数','','',0),(201,'p.sampling_ex','',15,'string','notice',0,1,'小流量统计参数','','',0),(202,'p.mapui_req_url','',15,'string','notice',0,1,'','','',0),(203,'p_uids','',16,'string','notice',0,1,'','','',0),(204,'p_uids','',15,'string','notice',0,1,'','','',0);
/*!40000 ALTER TABLE `log_module_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_dimension`
--

DROP TABLE IF EXISTS `schema_dimension`;
CREATE TABLE `schema_dimension` (
  `dimension_id` int(11) NOT NULL auto_increment,
  `dimension_name` varchar(255) character set gbk NOT NULL,
  PRIMARY KEY  (`dimension_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `schema_dimension`
--

LOCK TABLES `schema_dimension` WRITE;
/*!40000 ALTER TABLE `schema_dimension` DISABLE KEYS */;
INSERT INTO `schema_dimension` VALUES (1,'用户维度'),(2,'吧维度'),(3,'用户与吧维度');
/*!40000 ALTER TABLE `schema_dimension` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_field_values`
--

DROP TABLE IF EXISTS `schema_field_values`;
CREATE TABLE `schema_field_values` (
  `value_id` int(11) NOT NULL auto_increment,
  `field_id` int(11) NOT NULL,
  `value` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `demo` varchar(255) default NULL,
  PRIMARY KEY  (`value_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `schema_field_values`
--

LOCK TABLES `schema_field_values` WRITE;
/*!40000 ALTER TABLE `schema_field_values` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_field_values` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_operation_log`
--

DROP TABLE IF EXISTS `schema_operation_log`;
CREATE TABLE `schema_operation_log` (
  `log_id` int(11) NOT NULL auto_increment,
  `username` varchar(255) NOT NULL,
  `operation` varchar(255) NOT NULL,
  `table_id` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `table_name` varchar(255) NOT NULL,
  PRIMARY KEY  (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=338 DEFAULT CHARSET=utf8 COMMENT='鏃ュ織琛';

--
-- Dumping data for table `schema_operation_log`
--

LOCK TABLES `schema_operation_log` WRITE;
/*!40000 ALTER TABLE `schema_operation_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_operation_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_table`
--

DROP TABLE IF EXISTS `schema_table`;
CREATE TABLE `schema_table` (
  `table_id` int(11) NOT NULL auto_increment,
  `table_name` varchar(255) character set gbk NOT NULL,
  `description` varchar(255) character set gbk NOT NULL,
  `dimension_id` int(11) NOT NULL,
  `data_source` varchar(255) character set gbk NOT NULL COMMENT '数据源',
  `data_range` varchar(255) character set gbk NOT NULL,
  `time_range` varchar(255) character set gbk NOT NULL,
  `time_remain` varchar(255) character set gbk NOT NULL,
  `data_dimension` varchar(255) default NULL,
  PRIMARY KEY  (`table_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COMMENT='元数据表列表';

--
-- Dumping data for table `schema_table`
--

LOCK TABLES `schema_table` WRITE;
/*!40000 ALTER TABLE `schema_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_table_field`
--

DROP TABLE IF EXISTS `schema_table_field`;
CREATE TABLE `schema_table_field` (
  `field_id` int(11) NOT NULL auto_increment,
  `field_name` varchar(255) character set gbk NOT NULL COMMENT '字段名称',
  `type` varchar(20) character set gbk NOT NULL COMMENT '字段类型',
  `description` varchar(255) character set gbk NOT NULL COMMENT '字段说明',
  `source_layer` varchar(255) default NULL,
  `table_id` int(11) NOT NULL COMMENT '属于哪个表',
  `demo` varchar(255) default NULL,
  `rule` varchar(255) default NULL,
  `relationship` int(2) default '0',
  `has_field_value` int(2) default '0',
  PRIMARY KEY  (`field_id`)
) ENGINE=InnoDB AUTO_INCREMENT=118 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `schema_table_field`
--

LOCK TABLES `schema_table_field` WRITE;
/*!40000 ALTER TABLE `schema_table_field` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_table_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_table_relation`
--

DROP TABLE IF EXISTS `schema_table_relation`;
CREATE TABLE `schema_table_relation` (
  `relation_id` int(11) NOT NULL auto_increment,
  `child_table_id` int(11) NOT NULL,
  `parent_table_id` int(11) NOT NULL,
  PRIMARY KEY  (`relation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COMMENT='各个元数据表之间的关系表';

--
-- Dumping data for table `schema_table_relation`
--

LOCK TABLES `schema_table_relation` WRITE;
/*!40000 ALTER TABLE `schema_table_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_table_relation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-12-17  3:28:29

DROP TABLE IF EXISTS `log_module_field_operation`;
CREATE TABLE `log_module_field_operation` (
  `operation_id` int(11) NOT NULL auto_increment,
  `field_id` int(11) NOT NULL COMMENT 'log_module_field表中的field_id字段,在修改和删除的操作下，该字段不能为null',
  `field_name` varchar(255) NOT NULL,
  `default` varchar(255) NOT NULL,
  `module_id` tinyint(4) NOT NULL COMMENT '模块id ',
  `data_type` varchar(255) NOT NULL,
  `item_type` varchar(255) NOT NULL,
  `log_version` int(11) NOT NULL,
  `is_require` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `rule` varchar(255) NOT NULL,
  `separator` varchar(255) NOT NULL,
  `enum_values` varchar(255) NOT NULL COMMENT '枚举值的所有值，用;分割',
  `enum_values_description` varchar(255) NOT NULL COMMENT '枚举值的描述用;分割',
  `operation` int(11) NOT NULL COMMENT '操作类型0是增加,1是修改,2是删除',
  `status` int(11) NOT NULL COMMENT '状态:0保存，1为提交',
  PRIMARY KEY  (`operation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*alter table log_module_field add enum_values varchar(255);*/

DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(255) NOT NULL ,
  `role` int(11) NOT NULL ,
  PRIMARY KEY  (`id`),
  UNIQUE `username_id` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `url_host_path`;
CREATE TABLE `url_host_path` (
  `host_path_id` int(11) NOT NULL auto_increment,
  `host` varchar(255) NOT NULL COMMENT '主机',
  `path` varchar(255) NOT NULL COMMENT '路径',
  `module_id` int(11) NOT NULL,
  PRIMARY KEY  (`host_path_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;



DROP TABLE IF EXISTS `url_action`;
CREATE TABLE `url_action` (
  `action_id` int(11) NOT NULL auto_increment,
  `host_path_id` int(11) NOT NULL ,
  `action_name` varchar(255) NOT NULL COMMENT '行为名称',
  `version` int(11) NOT NULL,
  PRIMARY KEY  (`action_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `url_action_keys`;
CREATE TABLE `url_action_keys` (
  `id` int(11) NOT NULL auto_increment,
  `action_id` int(11) NOT NULL ,
  `key_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `url_keys`;
CREATE TABLE `url_keys` (
  `key_id` int(11) NOT NULL auto_increment,
  `module_id` int(11) NOT NULL,
  `precondition` varchar(255) COMMENT 'key含义的前置条件，用于兼容老的代码，key的含义已经重复定义的情况',
  `key` varchar(255) NOT NULL ,
  `key_description` varchar(255) ,
  `operation` tinyint(1) NOT NULL COMMENT '定义的操作的类型，0:相等,1:存在,2:正则匹配',
  `value` varchar(255) NOT NULL ,
  `value_description` varchar(255) ,
  PRIMARY KEY  (`key_id`),
  KEY `module_key_value` (`module_id`,`key`,`value`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;




