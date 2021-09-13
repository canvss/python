# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/23 15:28
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
Manager
Programmer
Salesman
get_salary
'''
from abc import abstractmethod,ABCMeta


class Employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def __init__(self,name):
        super().__init__(name)

    def get_salary(self):
        return 15000


class Programmer(Employee):
    def __init__(self,name,hour=0):
        super().__init__(name)
        self._hour = hour

    @property
    def hour(self):
        return self._hour
    @hour.setter
    def hour(self,h):
        self._hour = h

    def get_salary(self):
        return 150*self.hour


def main():
    p = Programmer('Endless',20)
    p.hour=25
    print(p.name,p.get_salary())
    man = Manager('JACK')
    print(man.name,man.get_salary())

if __name__ == '__main__':
    main()