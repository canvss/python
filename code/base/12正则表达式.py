# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/29 12:37
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
import re


def main():
    username = input('用户名：')
    m1 =  re.match('^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('username erro')

if __name__ == '__main__':
    main()