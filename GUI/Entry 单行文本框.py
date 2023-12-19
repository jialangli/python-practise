# 李佳朗
# 开发时间：2023
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.creatWidget()
    def creatWidget(self):
        #创建登录界面的组件
        self.label01=Label(self,text="密码")
        self.label01.pack()
        #StringVar变量绑定到指定的组件
        #StringVar变量的值发生变化，组件内容也变化
        v1=StringVar()
        self.entry01=Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())
        self.btn01=Button(self,text="登录",command=self.login)
        self.btn01.pack()
    def login(self):
        print("用户名：",self.entry01.get())
        messagebox.showinfo("系统","登录成功")
if __name__=='__main__':
    root=Tk()
    root.geometry("400x130+200+300")
    app=Application(master=root)
    root.mainloop()