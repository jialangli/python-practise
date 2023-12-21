# 李佳朗
# 开发时间：2023
#coding=utf-8
from socket import *
#最简化的UDP服务端代码
s=socket(AF_INET,SOCK_DGRAM) #创建UDP类型的套接字
addr=("127.0.0.1",8888) #绑定端口，ip可以不写
data=input("请输入：")
s.sendto(data.encode("gbk"),addr)
s.close()