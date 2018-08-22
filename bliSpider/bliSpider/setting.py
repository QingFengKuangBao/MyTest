
# ------------------------获取用户基本信息-----------------start
max_pn=100
m_d_url="https://api.bilibili.com/x/web-interface/newlist?rid={}&pn={}&ps=50"

# 音乐区的rid
map_rid={'原创音乐':28,'翻唱':31,"VOCALOID·UTAU":30,'演奏':59,'三次元音乐':29,'音乐选集':130,'OP\ED\OST':54,'宅舞':20,'三次元舞蹈':154,'舞蹈教程':156}
rid=[28,31,30,59,29,130,54,20,154,156]
# 舞蹈区的rid
# dance_rid={'宅舞':20,'三次元舞蹈':154,'舞蹈教程':156}

type=['new','hot']
max_page_num=200
get_type=['Photo','Doc']
# 摄影
photo_category=['cos','sifu']
photo_url='https://api.vc.bilibili.com/link_draw/v2/Photo/list?category={}&type={}&page_num={}&page_size=20'
# 画友
draw_category=['all','comic','illustration','draw']
draw_url='https://api.vc.bilibili.com/link_draw/v2/Doc/list?category={}&type={}&page_num={}&page_size=20'

# ------------------------获取用户基本信息-----------------end



# ------------------------数据库配置信息-----------------start

db_config = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "resource",
    'charset':'utf8mb4',
}

# ------------------------数据库配置信息-----------------end


import logging
import time
import os
# ------------------------日志配置信息-----------------start

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Log等级总开关

# 第二步，创建一个 file handler，用于写入日志文件
rq = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))

# 所有级别的日志输出
log_path = os.getcwd() + '/docs/Logs/all/'
log_name = log_path + rq + '_all.log'
logfile = log_name
if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(logfile):
    f=open(logfile,mode='w',encoding="utf-8")
    f.close()
fh_all = logging.FileHandler(logfile, mode='a',encoding='utf-8')
fh_all.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# debug以上日志handler
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.getcwd() + '/docs/Logs/debug/'
log_name = log_path + rq + '_debug.log'
logfile = log_name
if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(logfile):
    f=open(logfile,mode='w',encoding="utf-8")
    f.close()
fh_debug = logging.FileHandler(logfile, mode='a',encoding='utf-8')
fh_debug.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
debug_filter=logging.Filter()
debug_filter.filter=lambda record:record.levelno ==fh_debug.level #只在文件写入WARNING级别的日志
fh_debug.addFilter(debug_filter)


# info以上日志handler
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.getcwd() + '/docs/Logs/info/'
log_name = log_path + rq + '_ifo.log'
logfile = log_name

if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(logfile):
    f=open(logfile,mode='w',encoding="utf-8")
    f.close()
fh_info = logging.FileHandler(logfile, mode='a',encoding='utf-8')
fh_info.setLevel(logging.INFO)  # 输出到file的log等级的开关
info_filter=logging.Filter()
info_filter.filter=lambda record:record.levelno ==fh_info.level #只在文件写入WARNING级别的日志
fh_info.addFilter(info_filter)

# warn以上日志handler
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.getcwd() + '/docs/Logs/warn/'
log_name = log_path + rq + '_warn.log'
logfile = log_name

if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(logfile):
    f=open(logfile,mode='w',encoding="utf-8")
    f.close()
fh_warn = logging.FileHandler(logfile, mode='a',encoding='utf-8')
fh_warn.setLevel(logging.WARNING)  # 输出到file的log等级的开关
warn_filter=logging.Filter()
warn_filter.filter=lambda record:record.levelno ==fh_warn.level #只在文件写入WARNING级别的日志
fh_warn.addFilter(warn_filter)

# warn以上日志handler
log_path = os.getcwd() + '/docs/Logs/error/'
log_name = log_path + rq + '_error.log'
logfile = log_name
if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(logfile):
    f=open(logfile,mode='w',encoding="utf-8")
    f.close()
fh_error = logging.FileHandler(logfile, mode='a',encoding='utf-8')
fh_error.setLevel(logging.ERROR)  # 输出到file的log等级的开关
error_filter=logging.Filter()
error_filter.filter=lambda record:record.levelno ==fh_error.level #只在文件写入WARNING级别的日志
fh_error.addFilter(error_filter)

# 控制台 handler 
ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG) #控制台输出的日志级别

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh_debug.setFormatter(formatter)
fh_info.setFormatter(formatter)
fh_warn.setFormatter(formatter)
fh_error.setFormatter(formatter)
ch.setFormatter(formatter)
fh_all.setFormatter(formatter)

# 第四步，将logger添加到handler里面
logger.addHandler(fh_debug)
logger.addHandler(fh_info)
logger.addHandler(fh_warn)
logger.addHandler(fh_error)
logger.addHandler(fh_all)
logger.addHandler(ch)
# ------------------------日志配置信息-----------------end