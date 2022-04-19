# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/19 21:24

'''
     使用b模式操作文件
'''

# with open('a.txt', mode='rb')as f:
#     res = f.read().decode('utf-8')
#     print(res)
#
# with open(r'a.txt', mode='wb')as f:
#     f.write('你好世界'.encode('utf-8'))
#
# with open(r'a.txt', mode='ab')as f:
#     f.write('hello world!!!'.encode('utf-8'))

# 使用while读取文件
# with open('c.txt', mode='rb')as f:
#     while True:
#         # f.read(size)指定每次读取字节大小
#         res = f.read(1024).decode('utf-8')
#         print(res)
#         if len(res):
#             break

# f.readline()读取一行数据
with open('c.txt',mode='rb')as f:
    res = f.readline().decode('utf-8')
    print(res)


# f.writelines() 将一个list循环写入文件中
with open('e.txt', mode='wb')as f:
    li = [
        'hello\n'.encode('utf-8'),
        '你好\n'.encode('utf-8')
    ]
    f.writelines(li)