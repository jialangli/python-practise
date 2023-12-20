# 李佳朗
# 开发时间：2023
import threading
import queue
import time

# 缓冲区，用于生产者和消费者之间的数据交换
buffer = queue.Queue(maxsize=5)

# 生产者线程函数
def producer():
    for i in range(10):
        item = f"商品 {i}"
        buffer.put(item)
        print(f"生产者生产了 {item}")
        time.sleep(1)

# 消费者线程函数
def consumer():
    while True:
        item = buffer.get()
        print(f"消费者消费了 {item}")
        time.sleep(2)
        buffer.task_done()

# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待生产者和消费者线程执行完毕
producer_thread.join()
consumer_thread.join()
