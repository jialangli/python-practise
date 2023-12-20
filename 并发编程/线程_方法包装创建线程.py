# 李佳朗
# 开发时间：2023
import threading
# 定义一个需要在新线程中执行的方法
def my_task():
    # 在这里编写方法的具体逻辑
    print("Hello, I'm running in a new thread!")

# 创建并启动新线程
thread = threading.Thread(target=my_task)
thread.start()

# 主线程执行其他任务
print("Hello from the main thread!")
