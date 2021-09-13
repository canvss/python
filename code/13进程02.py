# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/29 13:27
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from multiprocessing import Process
from time import sleep

count = 0
def sub_task(string):
    global count
    while count<10:
        print(string,end='',flush=True)
        count+=1
        sleep(0.01)

def main():
    Process(target=sub_task,args=('Ping',)).start()
    Process(target=sub_task,args=('Pong',)).start()
if __name__ == '__main__':
    main()