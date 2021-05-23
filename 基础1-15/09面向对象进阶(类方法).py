# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/22 18:25
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
import os
from time import time, localtime, sleep


# 定义一个类描述数字时钟。
class Clock():
    def __init__(self, t, m, s):
        self._t = t
        self._m = m
        self._s = s

    def run(self):
        if self._s<60:
            self._s+=1
        if self._s == 60:
            self._m+=1
            self._s=0
            if self._m == 60:
                self._t+=1
                self._m =0
                if self._t == 24:
                    self._t=0
    @classmethod
    def now(cls):
        n_time=localtime(time())
        return cls(n_time.tm_hour,n_time.tm_min,n_time.tm_sec)

    def show(self):
        return ('%02d:%02d:%02d' % (self._t, self._m, self._s))


if __name__ == '__main__':
    os.system('clear')
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        os.system('clear')
        clock.run()