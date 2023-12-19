# 李佳朗
# 开发时间：2023
from tkinter import *
root = Tk()
root.geometry("700x220")
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
btnText = ("哈哈哈", "啦啦啦", "嘻嘻嘻", "哇哇哇")
for txt in btnText:
    Button(f1, text=txt).pack(side="left", padx=10)
for i in range(1, 13):
    Label(f2, width=5, height=10, borderwidth=1, relief="solid",
          bg="black" if i % 2 == 0 else "white").pack(side="left", padx=2)
root.mainloop()

