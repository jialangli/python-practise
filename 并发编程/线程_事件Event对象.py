# 李佳朗
# 开发时间：2023
import threading

# 创建一个事件对象
event = threading.Event()

def worker():
    print("等待事件触发...")
    event.wait()  # 等待事件触发
    print("事件已触发，继续执行后续操作。")

# 创建工作线程
t = threading.Thread(target=worker)

# 启动线程
t.start()

# 模拟一段时间后事件触发
# 在主线程中调用 event.set() 来触发事件
print("主线程执行一些操作...")
event.set()  # 触发事件

# 等待线程结束
t.join()
