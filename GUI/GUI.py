# 李佳朗
# 开发时间：2023
#tkinter介绍
from tkinter import *
from tkinter import messagebox
#导入了tkinter模块及其子模块messagebox，使我们能够使用这些模块提供的功能。
root=Tk()
#创建了一个Tk对象，该对象代表了我们的GUI应用程序的主窗口。
btn01=Button(root)
btn01["text"]="点我就送花"
btn01.pack()
#创建了一个按钮对象btn01，并将其放置在主窗口上。
# 设置了按钮的文本为"点我就送花"，然后将按钮放置在主窗口上。
def songhua(e):
    messagebox.showinfo("Message","送你一朵玫瑰花")
    print("送你99朵玫瑰花")
#定义了一个名为songhua的函数，它接受一个参数 e（表示事件）。在函数内部，使用messagebox.showinfo()方法显示一个弹窗，弹窗标题为"Message"，
# 弹窗内容为"送你一朵玫瑰花"。然后，在控制台输出一条信息"送你99朵玫瑰花"。
btn01.bind("<Button-1>",songhua)
#将按钮btn01与函数songhua绑定，当按钮被点击时，将执行songhua函数。
root.mainloop()#调用组件的mainloop()方法，进入事件循环