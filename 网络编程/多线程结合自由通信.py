# 李佳朗
# 开发时间：2023
#coding=utf-8
from socket import *
from threading import Thread
def recv_data():
    while True:
        recv_data = s.recvfrom(1024)
        recv_content = recv_data[0].decode('gbk')
        print(f"收到远程信息：{recv_content},from{recv_data[1]}")
        if recv_content == "88":
            print("结束聊天！")
            break
def send_data():
    addr=("127.0.0.1",8888)
    while True:
        data=input("请输入：")
        s.sendto(data.encode("gbk"),addr)
        if data=="88":
            print("结束聊天！")
            break

if __name__ == '__main__':
    s=socket(AF_INET,SOCK_DGRAM)  #创建UDP类型的套接字
    s.bind(("127.0.0.1",8888))    #绑定端口，IP可以不写
    #创建两个线程
    t1=Thread(target=recv_data)
    t2=Thread(target=recv_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()