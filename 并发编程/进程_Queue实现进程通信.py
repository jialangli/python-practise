# 李佳朗
# 开发时间：2023
import multiprocessing

def producer(queue):
    for i in range(5):
        item = f'Item {i}'
        queue.put(item)
        print(f'Produced: {item}')

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Consumed: {item}')

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    # 创建生产者进程和消费者进程
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    # 启动进程
    producer_process.start()
    consumer_process.start()

    # 等待生产者进程结束
    producer_process.join()

    # 向队列发送一个 None 值，表示数据已经全部生产完毕
    queue.put(None)

    # 等待消费者进程结束
    consumer_process.join()
