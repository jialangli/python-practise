# 李佳朗
# 开发时间：2023
#coding=utf-8
from socket import *

def close(sockets):
  for i in sockets:
    i.close()
  
server_socket=socket(AF_INET,SOL_SOCKET) #建立TCP套接字
server_socket.bind(("127.0.0.1",8899)) #本机监听8899端口
server_socket.listen(5)
print("等待接收连接！")
client_socket,client_info=server_socket.accept()
recv_data=client_socket.recv(1024) #最大接收1024字节
print(f"收到信息：{recv_data.decode('gbk')}m来自：{client_info}")

close([client_socket,server_socket])


