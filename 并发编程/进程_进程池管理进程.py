# 李佳朗
# 开发时间：2023
import multiprocessing

def worker(task):
    print(f'Executing task: {task}')
    # 在这里执行具体的任务

if __name__ == '__main__':
    # 创建进程池，指定池子中的进程数量为 3
    pool = multiprocessing.Pool(processes=3)

    tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']

    # 使用进程池执行任务
    pool.map(worker, tasks)

    # 关闭进程池
    pool.close()
    # 等待所有任务完成
    pool.join()
