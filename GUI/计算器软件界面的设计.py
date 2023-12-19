# 李佳朗
# 开发时间：2023
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        #通过grid布局实现计算机的界面
        binText=(("MC","M+","M-","MR"),
                 ("C","a","/","×"),
                 (7,8,9,"-"),
                 (4,5,6,"+"),
                 (1,2,3,"="),
                 (0,"."))
        Entry(self).grid(row=0,column=0,columnspan=4)
        for rindex,r in enumerate(binText):
            for cindex,c in  enumerate(r):
                if c=="=":
                    Button(self,text=c,width=2)\
                    .grid(row=rindex+1,column=cindex,rowspan=2,sticky="NSEW")
                elif c==0:
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, columnspan=2, sticky="NSEW")
                elif c==".":
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex+1, sticky="NSEW")
                else:
                    Button(self,text=c,width=2).grid(row=rindex+1,column=cindex,sticky="NSEW")

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200+200+300")
    app = Application(master=root)
    root.mainloop()