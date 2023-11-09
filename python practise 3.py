#猜数字游戏
import random
answer=random.randint(1,100)
count=0
while True:
    count+=1
    number=int(input("请输入数字"))
    if number==answer:
        print("恭喜，你答对了")
        break
    elif number>answer:
        print("小一点")
    else:
        print("大一点")


