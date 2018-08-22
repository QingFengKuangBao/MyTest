
import tkinter as tk
from tkinter import ttk
from tkinter import *

def test01():
    window = tk.Tk()
    window.title("tkinter")
    window.geometry('600x500')

    var = tk.StringVar()
    l = ttk.Label(master=window, textvariable=var,
                  background="red", font=("Aria", 40), width=20)
    l.pack()

    on_hid = False

    def hid_me():
        nonlocal on_hid  # 函数使用和修改外层的变量 nonlocal   函数使用和修改全局的变 global
        if on_hid:
            on_hid = False
            var.set("")
        else:
            on_hid = True
            var.set("hello\n world")

    b = ttk.Button(master=window, text="隐藏", width=20, command=hid_me, style=ttk.Style().configure("TButton", padding=5,font=("Aria", 20), relief="flat",background="#ccc"))

    b.pack()
    window.mainloop()



def test02():
    window = tk.Tk()
    window.title("tkinter")
    window.geometry('600x500')

    e=ttk.Entry(window,show="*")
    e.pack()

    def insert_point():
        var=e.get()
        t.insert('insert',var)

    def insert_end():
        var=e.get()
        t.insert('end',var)        

    b = tk.Button(master=window, text="point", width=20, command=insert_point,height=2 )
    b.pack()

    b1 = tk.Button(master=window, text="end", width=20, command=insert_end,height=2 )
    b1.pack()
    t=tk.Text(window,width=20,height=5)
    t.pack()
    
    window.mainloop()

def test03():
    window = tk.Tk()
    window.title("tkinter")
    window.geometry('600x500')
    var1=tk.StringVar()
    l1=tk.Label(window,width=10,height=2,textvariable=var1,font=("Aria", 15),bg='red')
    l1.pack()

    def show_select():
        show=lbox.get(lbox.curselection())
        var1.set(show)

    b=tk.Button(window,text="show",font=("Aria", 15),command=show_select)
    b.pack()

    var2=tk.StringVar()
    var2.set((11,88,99,51,3))
    lbox=tk.Listbox(window,listvariable=var2,font=("Aria", 15))
    list_item=['one','two','three']
    for item in list_item:
        lbox.insert('end',item)
    lbox.pack()
    window.mainloop()

if __name__ == '__main__':
    # test01()

    # test02()

    # test03()


    pass
