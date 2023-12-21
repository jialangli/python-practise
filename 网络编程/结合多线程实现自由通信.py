# 李佳朗
# 开发时间：2023
# 导入必要的库
from socket import *
from threading import Thread

# 接收数据的函数
def recv_data():
    while True:
        recv_data = client_socket.recv(1024)  # 接收数据，每次最多接收1024字节
        print(f"收到远程信息：{recv_data.decode('gbk')}")  # 打印接收到的信息
        if recv_data == b"end":  # 如果接收到 "end"，则退出循环
            break
# 发送数据的函数
def send_data():
    while True:
        msg = input(">")  # 输入要发送的消息
        client_socket.send(msg.encode("gbk"))  # 发送消息到服务器
        if msg == "end":  # 如果输入为 "end"，则退出循环
            break

if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
    client_socket.connect(("127.0.0.1", 8899))  # 连接到服务器的IP地址和端口号

    # 创建两个线程，一个用于接收数据，一个用于发送数据
    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)

    t1.start()  # 启动接收数据的线程
    t2.start()  # 启动发送数据的线程

    t1.join()  # 等待接收数据的线程结束
    t2.join()  # 等待发送数据的线程结束

    client_socket.close()  # 关闭套接字连接

