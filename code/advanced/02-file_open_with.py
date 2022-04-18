# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/18 23:08

# 写入文件
with open('c.txt', 'wt', encoding='utf-8') as f:
    f.write('hello world!!\n')

# 读取文件
with open('c.txt', 'rt', encoding='utf-8') as f:
    res = f.read()
    print(res)

# 追加写入
with open('c.txt', 'at', encoding='utf-8')as f:
    f.write('你好世界!')
