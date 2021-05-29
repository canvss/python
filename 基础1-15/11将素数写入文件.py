# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/28 22:56
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from math import sqrt

'''
将<50素数写入a.txt，
50<100写入b.txt
100-150写入c.txt
'''

# 判断是否为素数
def is_prime(n):
    assert n>0
    for x in range(2,int(sqrt(n)+1)):
        if n%x==0:
            return False
    return True if n !=1 else False

def main():
    file_name=('a.txt','b.txt','c.txt')
    fs_list=[]
    try:
        for fn in file_name:
            fs_list.append(open(fn,'w',encoding='utf-8'))
        for num in range(1,150):
            if is_prime(num):
                if num > 100:
                    fs_list[2].write(str(num)+'\n')
                if num < 50:
                    fs_list[0].write(str(num)+'\n')
                if num >50:
                    fs_list[1].write(str(num)+'\n')
    except IOError as ex:
        print(ex)
        print('写入出错')
    finally:
        for fs in fs_list:
            fs.close()
    print('over')

if __name__ == '__main__':
    main()