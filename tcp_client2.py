from socket import socket

# 创建套接字
tcp_socket = socket()

ADDR = ("127.0.0.1", 8888)

# 连接服务端
tcp_socket.connect(ADDR)

# 循环发送
while True:
    msg = input(">>> ")
    tcp_socket.send(msg.encode())

    # 接收服务端的消息
    data = tcp_socket.recv(1024)
    print("服务端：", data.decode())

# 关闭连接
tcp_socket.close()
