# 李佳朗
# 开发时间：2023
class __init__(self,master=None):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()#调用self.pack()方法，将窗口自身打包，使其显示在屏幕上。
        self.createWidget()#调用self.createWidget()方法，用于创建窗口中的各种组件。
    def createWidget(self):
        #创造组件
        self.btn01=Button(root,text="登录",
                          width=6,height=3,anchor=NE,command=self.login)
        self.btn01.pack()
        global photo
        photo=PhotoImage(file="")
        self.btn02=Button(root,image=photo,command=self.login)
        self.btn02.pack()
        self.btn02.config(state="disabled") #设置按钮为禁用

