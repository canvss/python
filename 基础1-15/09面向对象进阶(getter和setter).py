# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/22 17:33
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
使用setter getter对属性进行操作，保证代码的安全性
'''
class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self,age):
        self._age =age
    @name.setter
    def name(self,name):
        self._name = name

    def pd(self):
        print('姓名：%s \n年龄：%d'%(self.name,self.age))

if __name__ == '__main__':
    per = Person('Endless',22)
    per.age=18
    per.pd()
