# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/6/27 19:34
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
def func01(x):
    if x > 0:
        func01(x-1)
        print(x)

if __name__ == '__main__':
    func01(3)