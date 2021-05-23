# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/22 18:00
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
# 静态方法
class Triangle(object):
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z
    # 静态方法 @staticmethod注解
    @staticmethod
    def is_void(x,y,z):
        return x+y>z and x+z>y and y+z>x
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def z(self):
        return self._z
    # 求三角学周长
    def get_area(self):
        return self.x+self.y+self.z
def main():
    x,y,z = 5,2,4
    if Triangle.is_void(x,y,z):
        t = Triangle(x,y,z)
        print(t.get_area())
    else:
        print('no is Triangle!!')

if __name__ == '__main__':
    main()