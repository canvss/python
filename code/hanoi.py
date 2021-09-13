# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/6/27 19:35
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

# 汉诺塔
def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print('%s to %s'%(a,c))
        hanoi(n-1,b,a,c)

if __name__ == '__main__':
    hanoi(3,'A','B','C')