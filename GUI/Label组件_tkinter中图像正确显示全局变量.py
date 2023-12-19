# 李佳朗
# 开发时间：2023
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text="冲冲冲", width=10, height=2, bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="李佳朗", width=10, height=2, bg="blue", fg="white")
        self.label02.pack()

        # 显示图像
        global photo  # 将photo声明为全局变量，以免在方法执行完毕后图像对象被销毁
        photo = PhotoImage(file=r"C:\Users\ljl20\Desktop\v2-eb23a54a322d3c797f277fb65b393c3f_b.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="哈哈", borderwidth=5, relief="solid", justify="right")
        self.label04.pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200+200+300")  # 调整了geometry方法的参数，修正了乘号(*)的错误
    app = Application(master=root)
    root.mainloop()



