



import os
import sys
sys.path.append(os.getcwd())

from bliSpider.spidercore import *
from bliSpider import setting
from bliSpider import userifo
from bliSpider.util import sql_util
from bliSpider.setting import logger
from tkinter import *
from PIL import Image
from bliSpider.GUI import *
if __name__ == '__main__':
    # userifo.basic_userifo('https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_6&rid=20&type=0&pn=1&ps=20').analysis_data()
    # 初始化 id
    
    # userifo.init_all_basicifo()

    # userifo_spider(mid=837470).analysis_data()
    # userifo.init_sql_userifo()
    # userifo.init_txt_userifo()
    # userifo.init_txt_to_sql_userifo()
    # userifo.init_txt_uservidoes()

    # userifo.init_sql_uservideo()

    # userifo.init_sql_userdoc()
    # doclist_spider('206089973').start()
    # logger.info('hello')
    # logger.debug('hello')
    # logger.warn('hello')
    # logger.error('hello')
    # app=App()


    img=Image.open('e:/桌面/305c1252735d1f2152cb8058c2d585924e56e5f6.jpg')
    # new_img = img.convert('F')
    # new_img.show()
    # img.show()
    print(img.size)
    w=img.height
    
    pass
        
