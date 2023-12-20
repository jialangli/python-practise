# 李佳朗
# 开发时间：2023
import multiprocessing
def child_process():
    print("这是子进程，进程ID为：", multiprocessing.current_process().pid)
def parent_process():
    print("这是父进程，进程ID为：", multiprocessing.current_process().pid)
    p = multiprocessing.Process(target=child_process)  # 创建子进程
    p.start()
    p.join()
if __name__ == '__main__':
    parent_process()
