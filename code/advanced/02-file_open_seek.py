# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/19 21:33

'''
    文件指针操作
'''

# with open('a.txt',mode='rb')as f:
#     res = f.read(3).decode('utf-8')     # 读取3个字节（bytes）
#     print(res)
#
# with open('a.txt', mode = 'rt', encoding='utf-8')as f:
#     res = f.read(3)             # 读取3个字符
#     print(res)
#
# with open('a.txt', mode = 'rb')as f:
#     f.seek(3,0)
#     print(f.tell())
#     print(f.read().decode('utf-8'))
#
#
# with open('a.txt', mode='rb') as f:
#     f.seek(3,1)
#     print(f.tell())
#     print(f.read().decode('utf-8'))

with open('a.txt', mode='rb')as f:
    f.seek(-3,2)
    print(f.tell())
    print(f.read().decode('utf-8'))