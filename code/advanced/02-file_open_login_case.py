# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/18 23:31
'''
    读取文件中的用户信息实现登录
'''

def register_user(name, pwd):
    with open('db.txt',mode='wt',encoding='utf-8')as f:
        f.write(name+':'+pwd+'\n')


def login(input_name, input_pwd):
    with open('db.txt',mode='rt',encoding='utf-8')as f:
        for i in f:
            name,pwd = i.strip().split(':')
            if input_name == name and input_pwd == pwd:
                print('Login successful')
        else:
            print('Login erro')


if __name__ == '__main__':
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    # register_user(name, pwd)
    login(name,pwd)
