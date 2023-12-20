# 李佳朗
# 开发时间：2023
import multiprocessing

class SquareProcess(multiprocessing.Process):
    def __init__(self, number):
        super(SquareProcess, self).__init__()
        self.number = number

    def run(self):
        result = self.number ** 2
        print(f"The square of {self.number} is {result}")

# 创建进程对象并启动
if __name__ == '__main__':
    number = 5  # 需要计算平方的数
    square_process = SquareProcess(number)
    square_process.start()
    square_process.join()
