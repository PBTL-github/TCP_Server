"""
1. 建立TCP套接字
2. 等待客户端连接
3. 接收图片内容
4. 保存图片
5. 终止连接
"""

from socket import socket
import time

ADDR = ("0.0.0.0", 8888)

# 创建套接字
socket = socket()
# 绑定IP
socket.bind(ADDR)

# 设置监听
socket.listen(5)

# 创建connfd
connfd, addr = socket.accept()

# 接收客户端的数据
data = connfd.recv(1024 * 1024)
file_name = "%d-%d-%d.jpg" % time.localtime()[:3]
with open(file_name, "wb") as f:
    f.write(data)

f.close()

# 关闭连接
connfd.close()
socket.close()
