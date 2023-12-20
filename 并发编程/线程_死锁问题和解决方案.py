# 李佳朗
# 开发时间：2023
import threading

# 创建锁的实例
mutex_knife = threading.Lock()
mutex_pot = threading.Lock()

def cook_with_deadlock(chef_name):
    if chef_name == "小明":
        with mutex_knife:
            print("小明拿到了刀。")
            with mutex_pot:
                print("小明拿到了锅。开始烹饪。")
                # 模拟做菜的过程
                print("小明完成了菜的制作。")
    elif chef_name == "小红":
        with mutex_pot:
            print("小红拿到了锅。")
            with mutex_knife:
                print("小红拿到了刀。开始烹饪。")
                # 模拟做菜的过程
                print("小红完成了菜的制作。")

# 创建两个厨师线程，分别代表小明和小红
chef1_thread = threading.Thread(target=cook_with_deadlock, args=("小明",))
chef2_thread = threading.Thread(target=cook_with_deadlock, args=("小红",))

# 启动线程
chef1_thread.start()
chef2_thread.start()

# 等待线程结束
chef1_thread.join()
chef2_thread.join()
