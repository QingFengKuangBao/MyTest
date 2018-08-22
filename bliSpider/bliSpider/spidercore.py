
import requests
import json
import threading
from bliSpider.util import sql_util
import os
class spideBasic(threading.Thread):
    # 初始化
    def __init__(self, url=None, headers=None, method='get', params=None, data=None,logger=None):
        threading.Thread.__init__(self)
        if headers is None:
            headers = {
                # 'Accept': 'application/json, text/plain, */*',
                # 'Accept-Encoding': 'gzip, deflate, br',
                # 'Accept-Language': 'zh-CN,zh;q=0.8',
                # 'Cache-Control': 'no-cache',
                # 'Connection': 'keep-alive',
                # 'Content-Length': '50',
                # 'Content-Type': 'application/x-www-form-urlencoded',
                # 'Cookie': 'fts=1526053144; LIVE_BUVID=3eb38091fa84d0f50fdde51de2344bd3; LIVE_BUVID__ckMd5=1731f6ba975f403c; rpdid=olwqlplxskdosixwlqkiw; sid=atkbcf17; UM_distinctid=16357c5cc310-0539e03a36f524-5d4e211f-100200-16357c5cc32464; im_seqno_11513273=420; im_local_unread_11513273=0; LIVE_PLAYER_TYPE=1; finger=81df3ec0; DedeUserID=11513273; DedeUserID__ckMd5=98b04318c44d040b; SESSDATA=2bd08e40%2C1534037322%2C765db082; bili_jct=2873da1534365908c3d236a2061b3cad; BANGUMI_SS_23797_REC=233412; CURRENT_QUALITY=64; im_notify_type_11513273=0; buvid3=9222C002-5071-42F1-BCC2-AF9F9AD39C68163014infoc; html5_player_gray=false; stardustvideo=0; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1531477485,1532094405,1532584342,1532585581; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1532585581; bp_t_offset_11513273=144908940983161132; _dfcaptcha=4bde95983eb5d0eb288253b3079defca; CNZZDATA2724999=cnzz_eid%3D343722762-1518954196-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1532589900',
                # 'Referer': 'https://space.bilibili.com/{}',
                # 'Host': 'space.bilibili.com',
                # 'Origin': 'https://space.bilibili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            }
        self.logger=logger
        self.headers=headers
        self.url = url
        self.method = method
        self.params = params
        self.data = data
        self.encoding="utf-8"
        self.session = requests.Session()
        self.text= None
        pass

    def get_url_content(self):
        with self.session.request(method=self.method, url=self.url, params=self.params, data=self.data,headers=self.headers) as rep:
            self.text=rep.content.decode(self.encoding)

    def analysis_data(self):
        pass

    def run(self):
        pass


from bliSpider.model import *
import logging
# 获取用户信息
# https://space.bilibili.com/ajax/member/GetInfo   post  data
class userifo_spider(spideBasic):

    # 初始化

    def __init__(self,mid,fp=os.getcwd()+'/docs/user_ifo.txt',lock=None):
        headers = {
            # 'Accept': 'application/json, text/plain, */*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.8',
            # 'Cache-Control': 'no-cache',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '50',
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'fts=1526053144; LIVE_BUVID=3eb38091fa84d0f50fdde51de2344bd3; LIVE_BUVID__ckMd5=1731f6ba975f403c; rpdid=olwqlplxskdosixwlqkiw; sid=atkbcf17; UM_distinctid=16357c5cc310-0539e03a36f524-5d4e211f-100200-16357c5cc32464; im_seqno_11513273=420; im_local_unread_11513273=0; LIVE_PLAYER_TYPE=1; finger=81df3ec0; DedeUserID=11513273; DedeUserID__ckMd5=98b04318c44d040b; SESSDATA=2bd08e40%2C1534037322%2C765db082; bili_jct=2873da1534365908c3d236a2061b3cad; BANGUMI_SS_23797_REC=233412; CURRENT_QUALITY=64; im_notify_type_11513273=0; buvid3=9222C002-5071-42F1-BCC2-AF9F9AD39C68163014infoc; html5_player_gray=false; stardustvideo=0; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1531477485,1532094405,1532584342,1532585581; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1532585581; bp_t_offset_11513273=144908940983161132; _dfcaptcha=4bde95983eb5d0eb288253b3079defca; CNZZDATA2724999=cnzz_eid%3D343722762-1518954196-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1532589900',
            'Referer': 'https://space.bilibili.com/{}',
            # 'Host': 'space.bilibili.com',
            # 'Origin': 'https://space.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        }
        url = 'https://space.bilibili.com/ajax/member/GetInfo'
        data = {"mid":mid}
        headers["Referer"] = headers["Referer"].format(mid)
        method = "post"
        self.mid=mid
        self.fp=fp
        self.lock=lock
        super(userifo_spider, self).__init__(
            url=url, headers=headers, method=method, data=data)
        


    def analysis_data(self):
        data=json.loads(self.text,encoding=self.encoding)
        udata=data.get('data')
        str=json.dumps(udata,ensure_ascii=False)
        # id=udata.get('mid')
        # name=udata.get('name')
        # face=udata.get('face')
        # birthday=udata.get('birthday')
        # sex=udata.get('sex')
        # regtime=udata.get('sex')
        # sign=udata.get('sign')
        # current_level=udata.get('level_info').get('current_level')
        # str=r"{},{},{},{},{},{},{},{}".format(id,name,face,birthday,sex,regtime,sign,current_level)
        self.lock.acquire()
        with open(self.fp,mode='a+',encoding=self.encoding) as f:
            f.write(str+'\n')
            f.close()
        self.lock.release()

        
        

    def run(self):
        self.get_url_content()
        logging.info("{} user_ifo  start.....".format(self.mid))
        self.analysis_data()
        logging.info("{} user_ifo  end.....".format(self.mid))


import time
# 获取up主的投稿视频
# url=https://space.bilibili.com/ajax/member/getSubmitVideos?mid=23085689&pagesize=30&tid=0&page=1&keyword=&order=pubdate
class submitvidoe_spider(spideBasic):

    # 初始化  
    
    def __init__(self,mid,url=None,page=1,pagesize=100,fp=os.getcwd()+'/docs/user_vidoes.txt',lock=None):
        self.format_url='https://space.bilibili.com/ajax/member/getSubmitVideos?mid={}&pagesize={}&tid=0&page={}&keyword=&order=pubdate'
        super(submitvidoe_spider,self).__init__(url=url)
        self.mid=mid
        self.pagesize=pagesize
        self.fp=fp
        self.lock=lock
    

    def analysis_data(self):
        page=1
        video_list=list()
        while True:
            self.url=self.format_url.format(self.mid,self.pagesize,page)
            print(self.url)
            self.get_url_content()
            data=json.loads(self.text).get('data')
            pages=data.get('pages')
            if pages==0:
                return
            video_list.append(data.get('vlist'))            
            page+=1
            if page>pages:
                break
            time.sleep(0.1)

        if len(video_list)<=0:
            return
        data_list=list()
        for videos in video_list:
            for v in videos:
                data = (v.get('aid'), 'https'+v.get('pic'), v.get('created'), v.get('length'), v.get('favorites'), v.get('play'),
                        v.get('video_review'), v.get('title'), v.get('description'), v.get('mid'))
                data_list.append(data)
        
        sql="insert ignore into user_video (aid,pic,created,length,favorites,play,video_review,title,description,mid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        sql_util.sql_executemany(sql,data_list)

        # map_data={'mid':self.mid,'video':video_list}
        # json_data=json.dumps(map_data,ensure_ascii=False)
        # self.lock.acquire()
        # with open(self.fp, mode='a+', encoding=self.encoding) as f:
        #     f.write(json_data+'\n')
        #     f.close()
        # self.lock.release()

    def run(self):
        logging.info('{} video ...start'.format(self.mid))
        self.analysis_data()
        logging.info('{} video ...end'.format(self.mid))


# 获取投稿相册
# url  https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=8366990&page_num=0&page_size=30&biz=all
class doclist_spider(spideBasic):
    # biz =all photo daily  draw
    def __init__(self,uid,url=None,page_num=0,pagesize=200,biz='all',headers=None,method='get',params=None,data=None):
        self.format_url='https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid={}&page_num={}&page_size={}&biz={}'
        super(doclist_spider,self).__init__(url=url,method=method)
        self.uid=uid
        self.pagesize=pagesize
        self.biz=biz
        self.page_num=page_num


    def analysis_data(self):
        doc_list=list()
        picture_list=list()
        while True:
            self.url=self.format_url.format(self.uid,self.page_num,self.pagesize,self.biz)
            self.get_url_content()
            items=json.loads(self.text).get('data').get('items')
            if items is None:
                return
            for i in items:
                doc_data=(i.get('doc_id'),i.get('title'),i.get('description').replace("[\ud800\udc00-\udbff\udfff\ud800-\udfff]", ""),i.get('ctime'),i.get('view'),i.get('like'),i.get('count'),i.get('poster_uid'))
                doc_list.append(doc_data)
                doc_id=i.get('doc_id')
                for p in i.get('pictures'):
                    img_src=p.get('img_src')
                    src_hash=hash(img_src)
                    p_data=(src_hash,img_src,p.get('img_width'),p.get('img_height'),p.get('img_size'),doc_id)
                    picture_list.append(p_data)
            if len(items)<200:
                break
            self.page_num+=1
        sql_doc="insert ignore into user_doc (doc_id,title,description,ctime,views,favorite,count,poster_uid) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_pic="insert ignore into doc_picture (src_hash,img_src,img_width,img_height,img_size,doc_id) values(%s,%s,%s,%s,%s,%s)"
        sql_util.sql_executemany(sql_doc,doc_list)
        # print(doc_list[0])
        sql_util.sql_executemany(sql_pic,picture_list)

    def run(self):
        logging.info('{} doc ...start'.format(self.uid))
        self.analysis_data()
        logging.info('{} doc ...end'.format(self.uid))


# 获取 动态
# https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=3311852&offset_dynamic_id=0
class dynamic_spider(spideBasic):

    def __init__(self,host_uid,url=None,headers=None,method='get',params=None,data=None):
        url='https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid={}&offset_dynamic_id=0'.format(host_uid)
        super(dynamic_spider,self).__init__(url=url,method=method)

    def analysis_data(self):
        pass

