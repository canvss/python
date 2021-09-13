# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/23 12:50
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
from abc import abstractmethod


class Pet(object):
    def __init__(self,name):
        self._name = name

    @abstractmethod
    def make_voice(self):
        pass
    @property
    def name(self):
        return self._name

class Dog(Pet):
    def __init__(self,name):
        super().__init__(name)
    def make_voice(self):
        print('%s,汪汪汪...'%self.name)

class Cat(Pet):
    def __init__(self,name):
        super().__init__(name)
    def make_voice(self):
        print('%s,喵喵喵...' % self.name)

def main():
    pet = [Cat('凯蒂'),Dog('旺财')]
    for p in pet:
        p.make_voice()

if __name__ == '__main__':
    main()