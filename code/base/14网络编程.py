# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/29 22:13
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象指定使用那种传输服务
    # family = AF_INET  -ipv4地址
    # family = AF_INET6 -ipv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET,type=SOCK_STREAM)
    # 2.绑定ip地址和端口
    server.bind(('127.0.0.1',6789))
    # 3.开始监听
    server.listen(512)
    print('服务器启动开始监听')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client,addr = server.accept()
        print(str(addr)+'连接到了服务器')
        # 5发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6断开连接
        client.close()

if __name__ == '__main__':
    main()
