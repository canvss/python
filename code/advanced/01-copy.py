# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/15 13:20
'''
    深浅拷贝
'''

import copy

li = [2,5,[3,9]]
li2 = li.copy()
li = [3,5,[7,8]]
print(li)
print(li2)
li3 = copy.deepcopy(li)
print(li3)