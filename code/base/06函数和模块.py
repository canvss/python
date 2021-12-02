# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python
# @File     :06函数和模块
# @Date     :2021/5/20 22:30
# @Author   :epover
# @Email    :endliss@sina.cn
# @Software :PyCharm
-------------------------------------------------
"""

# 判断一个数是不是回文
def is_Palindromic (num):
    temp = num
    is_temp = 0
    while temp > 0:
        is_temp=is_temp*10+temp%10
        temp//=10
    return is_temp

# nu = 12353221
# if is_Palindromic(nu)==nu:
#     print("yes")
# else:
#     print('no')


# 判断一个数字是不是素数，在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
def is_Prime(num):
    for x in range(2,int(num**0.5)+1):
        if num%x == 0:
            return False
    return True if num!=1 else False    #num不能为1
is_p = is_Prime(5)
if is_p:
    print('yes')
else:
    print('no')

def test_fun_var():
    # global a    #将a定义为全局变量
    # a=100
    print('test_fun_var=',a)



if __name__ == '__main__':
    a=200
    test_fun_var()
    print('main a = ',a)