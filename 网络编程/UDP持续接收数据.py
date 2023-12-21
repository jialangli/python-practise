# 李佳朗
# 开发时间：2023
#coding=utf-8
from socket import *
#最简化的UDP服务端代码
s=socket(AF_INET,SOCK_DGRAM)  #创建UDP类型的套接字
s.bind("127.0.0.1",8888) #绑定端口，ip可以不写
print("等待接收数据！")
while True:
    recv_data=s.recvfrom(1024)
    recv_content=recv_data[0].decode('gbk')
    print(f"收到远程信息：{recv_content},from{recv_data[1]}")
    if recv_content=="88":
        print("结束聊天！")
s.close()