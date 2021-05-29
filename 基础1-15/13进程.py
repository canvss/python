# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/29 13:04
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from multiprocessing import Process
from time import time,sleep
from random import randint


def download_task(filename):
    print('开始下载%s'%filename)
    time_douwnload = randint(5,10)
    sleep(time_douwnload)
    print('%s下载完成！耗时%.2f秒'%(filename,time_douwnload))
    pass


def main():
    start = time()
    #  普通
    # download_task('python.exe')
    # download_task('学生.avi')

    # 利用进程
    p1 = Process(target=download_task,args=('Python.exe',))
    p1.start()
    print('进程id=',p1.pid,p1.name)
    p2 = Process(target=download_task,args=('学生.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总耗时：%.2f秒'%(end-start))


if __name__ == '__main__':
    main()