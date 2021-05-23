# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/23 12:26
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    @name.setter
    def name(self,name):
        self._name = name

    def watch_av(self):
        if self.age>=18:
            print('%s 正在看av'%self.name)
        else:
            print('%s 正在看熊出没。。'%self.name)

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade

    def study(self,course):
        print('%s的%s,正在学习%s'%(self.grade,self.name,course))

class Teacher(Person):
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self._title = title
    @property
    def title(self):
        return self._title
    def teach(self,course):
        print('%s%s正在教%s' %(self.title,self.name,course))



def main():
    stu = Student('Endless',17,'初三')
    stu.study('Python')
    stu.watch_av()
    te = Teacher('jake',25,'专家')
    te.teach('面向对象编程')
    te.watch_av()


if __name__ == '__main__':
    main()