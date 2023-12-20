# 李佳朗
# 开发时间：2023
import multiprocessing

def worker(shared_list):
    for i in range(5):
        shared_list.append(i)
        print(f'Worker: added {i} to shared list')
    shared_list.append(None)

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    shared_list = manager.list()

    # 创建工作进程
    worker_process = multiprocessing.Process(target=worker, args=(shared_list,))

    # 启动进程
    worker_process.start()

    # 等待工作进程结束
    worker_process.join()

    # 打印共享列表的内容
    print(f'Shared List: {shared_list}')
