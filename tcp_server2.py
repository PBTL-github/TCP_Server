from socket import socket, AF_INET, SOCK_STREAM

tcp_socket = socket(AF_INET, SOCK_STREAM)

ADDR = ("0.0.0.0", 8888)

tcp_socket.bind(ADDR)

tcp_socket.listen(5)


# 等待接收客户端的连接
print("等待客户端连接中...")
while True:
    connfd, addr = tcp_socket.accept()
    print("连接的客户端是: ", addr)

    data = connfd.recv(1024)

    print("消息：", data.decode())

    # 回复客户端
    connfd.send("已经收到".encode())
    connfd.close()


# 关闭连接
tcp_socket.close()