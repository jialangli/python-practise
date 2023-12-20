# 李佳朗
# 开发时间：2023
import threading

count = 0
lock = threading.Lock()  # 创建互斥锁

def increment():
    global count
    for _ in range(1000000):
        lock.acquire()  # 获取互斥锁
        count += 1
        lock.release()  # 释放互斥锁

def decrement():
    global count
    for _ in range(1000000):
        lock.acquire()  # 获取互斥锁
        count -= 1
        lock.release()  # 释放互斥锁

thread_a = threading.Thread(target=increment)
thread_b = threading.Thread(target=decrement)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print(count)

