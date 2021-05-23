# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python
# @File     :07字符串和常用数据结构
# @Date     :2021/5/21 19:16
# @Author   :epover
# @Email    :endliss@sina.cn
# @Software :PyCharm
-------------------------------------------------
"""


# print('hello \n wor\tld')
import os
import random

test = 'hello '*3
print(test)
print(test[2])
print('hello '+'world')
for i in 'hello':
    print(i)

a,b = 5,10
print('a=%d,b=%d,sum=%d'%(a,b,a+b))
print(f'{a}*{b}={a*b}')
os.system('clear')



"""
  生成指定长度的验证码
  :param code_len: 验证码的长度(默认4个字符)
  :return: 由大小写英文字母和数字构成的随机验证码
  """
def get_generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code =' '
    last_pos=len(all_chars)-1
    for x in range(code_len):
        index = random.randint(0,last_pos)
        code+=all_chars[index]
    return code

print(get_generate_code())


# 设计一个函数返回给定文件名的后缀名
def get_suffix(name,has_dot =False):
    suffix_in = name.rfind('.')
    if 0<suffix_in< len(name):
        index = suffix_in if has_dot else suffix_in+1
        return name[index:]
    else:
        return ""
suffix = get_suffix('zhasbfafbu.txt')
print('后缀名为：',suffix)


# 返回最大值
def get_max(args):
    args_temp = args[0]
    for n in args:
        if args_temp<n:
            args_temp = n
    return args_temp
list_s = [20,5,44,67,21]
print(get_max(list_s))

# 设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    # 如果x[0]>x[1],m1=x[0],m2[x1],否则m1=x[1],m2=[x0]
    m1,m2 = ((x[0],x[1]) if x[0]>x[1] else (x[1],x[0]))
    for n in range(2,len(x)):
        if x[n]>m1:
            m2 = m1
            m1 = x[n]
        elif x[n]>m2:
            m2 = x[n]
    return m1,m2

print(max2(list_s))


# 计算指定的年月日是这一年的第几天
def is_leap_year(year):
    return year%4==0 and year%100!=0 or year%400==0
def which_day(year,month,day):
    days_of_month = [
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(year)]
    total = 0
    for x in range(month-1):
        total+=days_of_month[x]
    return total+day
def main():
    print(which_day(1980,11,28))
if __name__ == '__main__':
    main()


def display(balls):
    # 返回key，vlaues
    for index, s in enumerate(balls):
        if index == len(balls)-1:
            print('|',end=' ')
        # 左边补0
        print('%02d' % s,end=' ')
    print()

def random_select():
    # 创建1-34列表
    st = [x for x in range(1,34)]
    # 将列表st通过sample返回6位随机数
    st_1 =  random.sample(st,6)
    # 升序
    st_1.sort()
    # 追加一位1-16随机数
    st_1.append(random.randint(1,16))
    return st_1
if __name__ == '__main__':
    n = int(input('机选几注： '))
    for _ in range(n):
        display(random_select())

