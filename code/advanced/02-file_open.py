# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/18 22:29

f = open('a.txt', 'rt', encoding='utf-8')
res = f.read()
# print(res)
f.close()


with open('db.txt','rt',encoding='utf-8')as f:
    for i in f:
        print(i)