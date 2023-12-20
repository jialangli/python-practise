# 李佳朗
# 开发时间：2023
import threading

count = 0

def increment():
    global count
    for _ in range(1000000):
        count += 1

def decrement():
    global count
    for _ in range(1000000):
        count -= 1

thread_a = threading.Thread(target=increment)
thread_b = threading.Thread(target=decrement)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print(count)
