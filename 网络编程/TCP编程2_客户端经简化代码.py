# 李佳朗
# 开发时间：2023
from socket import *
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(("127.0.0.1",8899))
client_socket.send("hello".encode("gbk"))
client_socket.close()