# 李佳朗
# 开发时间：2023
import threading

# 创建一个信号量对象
semaphore = threading.Semaphore(2)  # 设置信号量的初始值为2

def work():
    semaphore.acquire()  # 获取资源前先申请信号量
    try:
        # 执行需要同步的代码块
        print("执行工作...")
    finally:
        semaphore.release()  # 释放资源后释放信号量

# 创建多个工作线程
threads = []
for _ in range(5):
    t = threading.Thread(target=work)
    threads.append(t)

# 启动线程
for t in threads:
    t.start()

# 等待线程结束
for t in threads:
    t.join()
