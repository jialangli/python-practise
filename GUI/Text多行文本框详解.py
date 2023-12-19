# 李佳朗
# 开发时间：2023
from tkinter import*
import webbrowser

class Application(Frame):
    def createWidget(self):
        self.w1 = Text(root, width=40, height=12, bg="gray")
        self.w1.pack()
        self.w1.insert(1.0, "0123456789\nabcdefg")
        self.w1.insert(2.3, "落霞与孤鹜齐飞\n")
        Button(self, text="重复插入文本", command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过tag精确控制文本", command=self.testTag).pack(side="left")

    def insertText(self):
        self.w1.insert(INSERT, "ljlang")
        self.w1.insert(END, '[sxt]')

    def returnText(self):
        print(self.w1.get(1.2, 1.6))
        self.w1.insert(1.8, "ljlang")
        print("所有文本内容:\n" + self.w1.get(1.0, END))

    def addImage(self):
        self.photo = PhotoImage(file="")
        self.w1.image_create(END, image=self.photo)

    def addWidget(self):
        b1 = Button(self.w1, text='啦啦啦')
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "good good study, day, day up!")
        self.w1.tag_config("baidu", underline=True)
        self.w1.tag_add("baidu", 4.0, 4.2)
        self.w1.tag_config("baidu", underline=True)
        self.w1.tag_bind("baidu", "<Button-1>", self.webshow)

    def testTag(self):  # 添加了testTag方法的实现
        print("通过tag精确控制文本")

    def webshow(self, event):
        webbrowser.open("http://www.baidu.com")

if __name__ == "__main__":
    root = Tk()
    root.geometry("450x300+200+300")
    app = Application(master=root)
    app.createWidget()
    root.mainloop()





