# 李佳朗
# 开发时间：2023
import threading

# 创建继承自Thread类的子类
class MyThread(threading.Thread):
    def run(self):
        # 在这里编写线程的具体逻辑
        print("Hello, I'm running in a new thread!")

# 创建并启动新线程
thread = MyThread()
thread.start()

# 主线程执行其他任务
print("Hello from the main thread!")
