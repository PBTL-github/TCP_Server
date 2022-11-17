from socket import *

# 创建TCP套接字  如果不写套接字参数 默认tcp  流式套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

ADDR = ("0.0.0.0", 8888)

# 绑定地址
tcp_socket.bind(ADDR)

# 设置监听  listen中的参数为最大链接次数  最多能设置1024      Linux是自动设置
# 具备了监听的属性   同时具备了被客户端链接的属性
tcp_socket.listen(5)


# 等待出来客户端的链接
# accept 阻塞函数  处理客户端连接请求  没有连接则阻塞
# connfd 专门处理该连接的套接字
# addr 客户端地址
print("等在客户端连接中...")
connfd, addr = tcp_socket.accept()
print("连接的客户端是: ", addr)


# 接受处理客户端的信息
data = connfd.recv(1024)
print("消息：", data.decode())

# 关闭连接
connfd.close()
tcp_socket.close()