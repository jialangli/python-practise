# 李佳朗
# 开发时间：2023
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    "一个经典的GUI程序的类的写法"
    def __init__(self,master=None):
        super().__init__(master)  #super()代表的是父类的定义，而不是父类对象
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        #创建组件
        self.btn01=Button(self)
        self.btn01["text"]='点击送花'
        self.btn01.pack()
        self.btn01["command"]=self.songhua
        #创建一个退出按钮
        self.btnQuit=Button(self,text='退出',command=root.destroy)
        self.btnQuit.pack()
    def songhua(self):
        messagebox.showinfo("送花","送你99朵玫瑰花")

if __name__ =='__main__':
    root=Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序类的测试")
    app=Application(master=root)
    root.mainloop()

# 以上代码示例是一个使用`tkinter`库编写的经典GUI程序类的例子。这个程序创建了一个窗口，包含一个按钮和一个退出按钮。
#
# 首先，导入`tkinter`库和`messagebox`模块。然后定义了一个名为`Application`的类，继承自`Frame`类，用于创建GUI应用程序的主要框架。
#
# 在类的`__init__`方法中，调用了父类`Frame`的构造函数，同时保存了`master`参数（即根窗口），并进行了一些初始化设置。
#
# `createWidget`方法用于创建组件。在这个方法中，首先创建了一个名为`btn01`的按钮，并设置其文本为"点击送花"，然后通过`pack`方法将按钮放置在窗口中。接着，为按钮的`command`属性绑定了一个回调函数`songhua`。
#
# 另外，还创建了一个名为`btnQuit`的退出按钮，并为其设置了文本和退出函数`root.distroy`，同样使用`pack`方法将其放置在窗口中。
#
# `songhua`函数是按钮`btn01`的回调函数，在点击按钮时会弹出一个消息框，显示"送你99朵玫瑰花"的信息。
#
# 在`__name__ == '__main__'`的判断中，创建了一个`Tk`对象作为根窗口`root`，并设置了窗口的大小和标题。随后，实例化了`Application`类的对象`app`，将根窗口作为参数传递给它。最后，调用`root.mainloop()`方法启动GUI程序的主事件循环。
#
# 通过运行这段代码，可以显示出一个包含按钮的窗口，点击按钮后会弹出一个消息框，显示"送你99朵玫瑰花"的消息。退出按钮可以关闭程序的窗口。
#
# 这个例子演示了一个经典的GUI程序类的写法，通过`tkinter`库可以方便地创建各种GUI应用程序。
#
