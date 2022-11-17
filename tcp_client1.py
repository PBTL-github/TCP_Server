from socket import socket, gethostbyname

# 创建套接字
tcp_socket = socket()

remote_ip = gethostbyname("www.baidu.com")
print(remote_ip)

ADDR = ("127.0.0.1", 8888)

# 连接服务端
tcp_socket.connect(ADDR)


# 发送消息
msg = input(">>> ")
tcp_socket.send(msg.encode())

# 关闭连接
tcp_socket.close()
