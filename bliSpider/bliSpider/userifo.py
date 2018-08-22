
import json
from bliSpider import setting as se
from bliSpider.spidercore import spideBasic
from bliSpider.model import user 
import os
import threading
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -%(threadName)s %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class basic_userifo(spideBasic):
    
    def __init__(self,url,threadlock=None):
        super(basic_userifo, self).__init__(url)
        self.lock=threadlock
        self.logger=logging.getLogger()

    def analysis_data(self,filepath):
        users=''
        data=json.loads(self.text,encoding=self.encoding)
        archives=data.get('data').get('archives')
        if archives is None:
            return
        u=user()
        for archive in archives:
            owner=archive.get("owner")
            u.id=owner.get("mid")
            u.name=owner.get("name").replace('\n',"")
            u.face=owner.get("face")
            users+="{},{},{}\n".format(u.id,u.name,u.face)
        self.lock.acquire()
        with open(filepath,mode="a+",encoding=self.encoding,closefd=True) as f:
            # print(users)
            f.write(users)
            f.close()
        self.lock.release()
    
    def analysis_data2(self,filepath):
        users=''
        data=json.loads(self.text,encoding=self.encoding)
        items=data.get('data').get('items')
        if items is None:
            return
        u=user()
        for item in items:
            iuser=item.get("user")
            u.id=iuser.get("uid")
            u.name=iuser.get("name")
            u.face=iuser.get("head_url")
            users+="{},{},{}\n".format(u.id,u.name,u.face)
        self.lock.acquire()
        with open(filepath,mode="a+",encoding=self.encoding,closefd=True) as f:
            # print(users)
            f.write(users)
            f.close()
        self.lock.release()

    def run(self):
        self.get_url_content()
        fp=os.getcwd()+"/docs/basic_ifo.txt"
        if os.path.exists(fp):
            os.remove(fp)
        self.logger.info("{} start ...".format(self.url))
        if self.url.startswith('https://api.bilibili.com/x/web-interface/newlist'):
            self.analysis_data(fp)
        if self.url.startswith('https://api.vc.bilibili.com/link_draw/v2/'):
            self.analysis_data2(fp)
        self.logger.info("{} end ...".format(self.url))



# 舞蹈音乐区初始化
def init_music_dance_ifo():
    lock=threading.Lock()
    for rid in se.rid:
        for pn in range(1,se.max_pn+1):
            url=se.m_d_url.format(rid,pn)
            t=basic_userifo(url,lock)
            t.start()
            time.sleep(0.1)

# 摄影区  初始化            
def init_photo_ifo():
    lock=threading.Lock()
    for catgory in se.photo_category:
        for page_num in range(se.max_page_num+1):
            url=se.photo_url.format(catgory,'new',page_num)
            t=basic_userifo(url,lock)
            t.start()
            time.sleep(0.1)

# 绘画区初始化
def init_draw_ifo():
    lock=threading.Lock()
    # for catgory in se.draw_category:
    for page_num in range(se.max_page_num+1):
        url=se.draw_url.format('all','new',page_num)
        t=basic_userifo(url,lock)
        t.start()
        time.sleep(0.1)


# 初始化 基本的用户信息 id name  写入 txt 文件
def init_txt_basicifo():
    init_draw_ifo()
    init_music_dance_ifo()
    init_photo_ifo()




from bliSpider.util import sql_util
def from_txt_to_sql(filepath):
    f=open(filepath,mode="r",encoding="utf-8",closefd=True)
    ulist=set()
    lines=f.readlines()
    index_max=len(lines)-1
    data=list()
    sql='insert ignore into basic_ifo (uid,name,face) values(%s,%s,%s)'
    i=0
    while True:
        line=lines[i].replace('\n','').split(',')
        ulist.add(user(line[0],line[1],line[2]))
        i=i+1
        if len(ulist)>=3000 or i>index_max:
            for u in ulist:
                data.append((u.id,u.name,u.face))
            sql_util.sql_executemany(sql,data)
            ulist.clear()
            data.clear()
        if i>index_max:
            break

# 初始化数据库 user 基本信息
def init_sql_basicifo():
    fp1=os.getcwd()+"/docs/basic_ifo.txt"
    from_txt_to_sql(fp1)


# 初始化 txt  数据库
def init_all_basicifo():
    init_txt_basicifo()
    init_sql_basicifo()

import time
from concurrent.futures import ThreadPoolExecutor
import  queue
from bliSpider.spidercore import userifo_spider


        
def init_txt_userifo():
    pool=ThreadPoolExecutor(40)
    id_map=sql_util.sql_execute('select uid from basic_ifo')
    fp=os.getcwd()+'/docs/user_ifo.txt'
    if not os.path.exists(fp):
        f=open(fp,mode="w",encoding='utf-8')
        f.close()

    with open(fp,mode="r",encoding='utf-8',closefd=True) as f:
        line_num=len(f.readlines())
        f.close()
    
    max_num=len(id_map)
    lock=threading.Lock()
    while True:
        u=userifo_spider(id_map[line_num].get('uid'),fp=fp,lock=lock)
        # u.start()
        pool.submit(u.start)
        line_num+=1
        if line_num>=max_num:
            break
        time.sleep(0.3)

            
def init_txt_to_sql_userifo():
    logging.info('userifo  用户数据  sql  初始化开始')
    sql='insert ignore into user_ifo (uid,name,face,birthday,sex,regtime,sign,current_level) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    fp=os.getcwd()+'/docs/user_ifo.txt'
    with open(fp,mode="r",encoding='utf-8',closefd=True) as f:
        lines=f.readlines()
        f.close()
    data_list=list()
    max_num=len(lines)
    num=0
    for line in lines:
        num+=1
        udata=json.loads(line)
        id=udata.get('mid')
        name=udata.get('name')
        face=udata.get('face')
        birthday=udata.get('birthday')
        sex=udata.get('sex')
        regtime=udata.get('regtime')
        sign=udata.get('sign')
        current_level=udata.get('level_info').get('current_level')
        data=(id,name,face,birthday,sex,regtime,sign,current_level)
        data_list.append(data)
        if len(data_list)>=2000 or num>=max_num:
            sql_util.sql_executemany(sql,data_list)
            data_list.clear()



from bliSpider.spidercore import submitvidoe_spider
def init_txt_uservidoes():
    pool=ThreadPoolExecutor(40)
    id_map=sql_util.sql_execute('select uid from basic_ifo')
    fp=os.getcwd()+'/docs/user_videos.txt'
    if not os.path.exists(fp):
        f=open(fp,mode="w",encoding='utf-8')
        f.close()

    with open(fp,mode="r",encoding='utf-8',closefd=True) as f:
        line_num=len(f.readlines())
        f.close()
    
    max_num=len(id_map)
    lock=threading.Lock()
    while True:
        u=submitvidoe_spider(id_map[line_num].get('uid'),fp=fp,lock=lock)
        # u.start()
        pool.submit(u.start)
        line_num+=1
        if line_num>max_num:
            break
        time.sleep(0.3)

# 初始化用户视频
def init_sql_uservideo():
    id_map=sql_util.sql_execute('select uid from basic_ifo')
    max_mid=sql_util.sql_execute('select mid from user_video order by mid DESC limit 1')

    for id in id_map:
        if len(max_mid)==0 or id.get('uid')>max_mid[0].get('mid'):
            submitvidoe_spider(id.get('uid')).start()
            time.sleep(0.3)


# 初始化用户相册
from bliSpider.spidercore import doclist_spider
def init_sql_userdoc():
    id_map=sql_util.sql_execute('select uid from basic_ifo')
    max_mid=sql_util.sql_execute('select poster_uid from user_doc order by poster_uid DESC limit 1')

    for id in id_map:
        if len(max_mid)==0 or id.get('uid')>max_mid[0].get('poster_uid'):
            doclist_spider(id.get('uid')).start()
            time.sleep(0.3)