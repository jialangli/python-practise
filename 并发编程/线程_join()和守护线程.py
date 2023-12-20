# 李佳朗
# 开发时间：2023
#join（）方法
import threading
import time
# 定义一个需要在新线程中执行的方法
def my_task():
    print("Thread started")
    time.sleep(2)  # 模拟耗时操作
    print("Thread finished")
# 创建并启动新线程
thread = threading.Thread(target=my_task)
thread.start()
# 主线程等待新线程执行完毕
thread.join()
# 主线程继续执行
print("Main thread continues")
