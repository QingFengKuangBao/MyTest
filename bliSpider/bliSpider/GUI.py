
import time
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mesgbox
from bliSpider.util import sql_util
class App(tk.Tk):

    def __init__(self):
        self.root=tk.Tk(sync=1)
        # self.root.geometry('600x400+200+100')
        self.data=None
        self.app_layout()
        self.createWidgets()
        self.root.mainloop()

    def app_layout(self):
        self.head=tk.LabelFrame(self.root,width=800,height=50)
        self.head.grid(row=0,columnspan=4,padx=5,pady=10)

        self.left=tk.LabelFrame(self.root,width=200,height=500)
        self.left.grid(row=1,column=0,padx=5)

        self.right=tk.LabelFrame(self.root,width=590,height=500)
        self.right.grid(row=1,column=1,columnspan=3,padx=5)
        
        self.foot=tk.LabelFrame(self.root,width=800,height=30)
        self.foot.grid(row=3,columnspan=4,padx=5,pady=3)

        pass

    def createWidgets(self):
        self.init_frame()
        pass




    def init_frame(self):

        tip_lable=ttk.Label(self.head,text="输入",font=('',14))
        tip_lable.place(x=10,y=10)

        explor_entry=tk.Entry(self.head,font=('',18),width=45)
        explor_entry.place(x=60,y=7)
        
        # id_radiobutton=tk.Radiobutton(self.head,text='ID',value='id')
        # name_radiobutton=tk.Radiobutton(self.head,text='name',value='name')
        # id_radiobutton.place(x=610,y=10)
        # name_radiobutton.place(x=650,y=10,)
        

        face_label=tk.Label(self.left,text='搜索结果',font=('',16))
        face_label.place(x=5,y=10)

        userifo=tk.StringVar(value='用户信息')
        ifo_label=tk.Label(self.right,textvariable=userifo,font=('',13))
        ifo_label.place(relwidth=1,relheight=0.1)
        
        user_listbox=tk.Listbox(self.left,font=('',13))
        user_listbox.place(x=5,y=40,relwidth=0.9,relheight=0.9)

        yscrollbar = tk.Scrollbar(user_listbox,command=user_listbox.yview)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        user_listbox.config(yscrollcommand=yscrollbar.set)

        
        def show_detail_ifo(e):
            index=video_listbox.curselection()
            item=video_listbox.get(index)
            id=int(item.split(':')[1])
            # print(id)
            if str(item).startswith('aid'):
                sql='select * from user_video where aid=%s'
                res=sql_util.sql_execute(sql,(id))
                # print(res)
                res=res[0]
                
                created=time.ctime(res['created'])
                mesg="aid:{}\ntitle:{}\ndesc:{}\n长度:{}\n上传时间:{}\n".format(res['aid'],res['title'],res['description'],res['length'],created)
                mesgbox.showinfo('视频信息',mesg)
                return
            elif str(item).startswith('doc_id'):
                sql='select * from user_doc where doc_id=%s'
                res=sql_util.sql_execute(sql,(id))
                res=res[0]
                ctime=time.ctime(res['ctime'])
                mesg="doc_id: {}\ntitle: {}\ndesc:{}\ncount:{}\n上传时间{}\n".format(res['doc_id'],res['title'],res['description'],res['count'],ctime)
                mesgbox.showinfo('相簿信息',mesg)
            else:
                return

        video_listbox=tk.Listbox(self.right,font=('',13))
        video_listbox.place(x=5,y=50,relwidth=1,relheight=0.9)
        v_yscrollbar = tk.Scrollbar(video_listbox,command=video_listbox.yview)
        v_yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        video_listbox.config(yscrollcommand=v_yscrollbar.set)
        video_listbox.bind('<Double-Button-1>',func=show_detail_ifo)


        def get_userifo(event):
            # print(event)
            index=user_listbox.curselection()
            item=user_listbox.get(index)
            if item=='' or item is None:
                return
            data=item.split(':')[1]
            # print(data)
            if data.isdigit():
                uid=int(data)
            else:
                # sql="select uid from user_ifo where name=%s"
                # res=sql_util.sql_execute(sql,data)
                # print(res[0].get('uid'))
                index=(index[0]-1,)
                uid=user_listbox.get(index).split(':')[1]
 
            sql='select birthday,sex,sign from user_ifo where uid=%s'
            user_ifo=sql_util.sql_execute(sql,(uid))
            print(user_ifo)
            if len(user_ifo)>0:
                userifo.set("生日:{}      性别:{}\n sign:{}".format(user_ifo[0]['birthday'],user_ifo[0]['sex'],user_ifo[0]['sign']))

            sql="SELECT uv.aid,uv.title FROM user_video AS uv WHERE uv.mid=%s"
            video_res=sql_util.sql_execute(sql,(uid))
            # print(video_res)
            video_listbox.delete(0,tk.END)
            if len(video_res)>0:
                video_listbox.insert(tk.END,'------视频-------')
                for v in video_res:
                    video_listbox.insert(tk.END,'aid:{}:{}'.format(v['aid'],v['title']))

            sql="SELECT doc_id,description FROM user_doc WHERE poster_uid=%s"
            doc_res=sql_util.sql_execute(sql,(uid))
            # print(doc_res)
            if len(doc_res)>0:
                video_listbox.insert(tk.END,'------相簿-------')
                for d in doc_res:
                    video_listbox.insert(tk.END,'doc_id:{}:{}'.format(d['doc_id'],d['description']))


        
        user_listbox.bind('<Double-Button-1>',func=get_userifo)

        def show():
            user_listbox.delete(0,tk.END)
            v=explor_entry.get().replace(' ','')
            if v.isdigit():
                v=int(v)
                sql='select uid,name from user_ifo where uid=%s'
            else:
                sql="select uid,name from user_ifo where name like '%%%s%%'"%(v)
                v=None
            res=sql_util.sql_execute(sql,(v))
            # print(res)
            str=''
            for r in res:
                for k in r: 
                    str="{}:{}".format(k,r.get(k))
                    user_listbox.insert(tk.END,str)
                user_listbox.insert(tk.END,'')
            user_listbox.insert(tk.END,'没有其他的了...')


        

        explore_button=tk.Button(self.head,text='搜索',font=('',15),relief=tk.RAISED,bd=4,command=show)
        explore_button.place(x=720,y=5)

    


if __name__ == '__main__':
    app=App()
