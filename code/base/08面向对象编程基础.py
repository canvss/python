# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Date     :2021/5/22 15:48
# @Author   :epover
# @Email    :endliss@sina.cn
-------------------------------------------------
"""
class Person(object):
    def __init__(self,foo):
        self.__foo = foo

    def eat(self):
        print('%s is eating！！'% self.__foo)
        pass
    def running(self):
        print('%s is running!!' % self.__foo)
        pass
    def __bar(self):
        print('this is praivte')



#  定义一个student类
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self):
        print('%s正在学习'%self.name)
    def watch_movie(self):
        if self.age>=18:
            print('%s正在看电视！！'%self.name)
        else:
            print('%s正在看动画片'%self.name)



if __name__ == '__main__':
    per = Person('jack')
    per.eat()
    per.running()
    stu = Student('zz',2)
    stu.study()
    stu.watch_movie()


