# 李佳朗
# 开发时间：2023
#coding=utf-8
from socket import *
server_socket=socket(AF_INET,SOL_SOCKET) #建立TCP套接字
server_socket.bind(("127.0.0.1",8899)) #本机监听8899端口
server_socket.listen(5)
print("等待接收连接！")
client_socket,client_info=server_socket.accept()
print("一个客户端建立连接成功")
while True:
    recv_data=client_socket.recv(1024) #最大接收1024字节
    print(f"收到信息：{recv_data.decode('gbk')}m来自：{client_info}")
    if recv_data=="end":
        break
        msg=input(">")
        client_socket.send(msg.encode("gbk"))
client_socket.close()
server_socket.close()