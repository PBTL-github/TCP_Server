"""
1. 创建套接字
2. 连接服务器
3. 读取文件内容
4. 发送内容
5. 关闭连接
"""

# 导入模块
from socket import socket

ADDR = ("127.0.0.1", 8888)

# 创建套接字
socket = socket()

# 连接服务端
socket.connect(ADDR)

# 读入文件内容
with open("1.jpg", "rb") as f:
    data = f.read()

# 发送内容
socket.send(data)

f.close()
socket.close()
