# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :python
# @File     :05
# @Date     :2021/5/19 20:21
# @Author   :epover
# @Email    :endliss@sina.cn
# @Software :PyCharm
-------------------------------------------------
"""
# 打印水仙花数
# 说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
# 该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
for n in range(100, 1000):
    x = int(n / 100)
    y = int((n - (x * 100)) / 10)
    z = int((n - x * 100 - y * 10))
    if x ** 3 + y ** 3 + z ** 3 == n:
        print(n)

# 实现数字反转
# 12345 54321
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)


# 生成斐波那契数列的前20个数。
# 形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
# list_l = []
# for n in range(20):
#     if n <= 1:
#         list_l.append(1)
#         continue
#     list_l.append(list_l[n-1]+list_l[n-2])
# print(list_l)

a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')

# 找出10000以内的完美数
# 例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
# list_pe = []
# for n in range(1,10000):
#     list_eve=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             list_eve.append(i)
#     list_eve.remove(n)
#     temp_s = 0
#     for l in list_eve:
#         temp_s+=l
#     if n == temp_s:
#         list_pe.append(n)
# print("完美数有：",list_pe)

import math

for num in range(1, 10000):
    result = 0
    # math.sqrt(100)=10 返回数字的平方根
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)

# 判断输入的正整数是不是回文数
# 回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
# num = int(input('请输入一个正整数: '))
# temp_n = num
# sum = 0
# while temp_n > 0 :
#     sum*=10
#     sum+=temp_n%10
#     temp_n//=10
#
# if num == sum:
#     print('yes')
# else:
#     print("no")


# 输出2~99之间的素数

# for i in range(2, 100):
#     for x in range(2, i):
#         if i % x == 0:
#             break
#         else:
#             print(i)


# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print('公鸡=', x, "  ", "母鸡=", y, "小鸡= ", z)

# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，
# 如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
from random import randint

money = 1000
while money > 0:
    print('你的余额为：',money)
    Next_f = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('你摇出骰子点数为：',first)
    if first == 7 or first == 11:
        money += debt
        print('恭喜你赢了：',debt)
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('很遗憾你输了：',debt)
    else:
        Next_f = True
    while Next_f:
        Next_f=False
        Next_rand =  randint(1,6)+randint(1,6)
        if Next_rand == 7:
            money-=debt
            print('很遗憾你输了：', debt)
        elif Next_rand == first:
            money+=debt
            print('恭喜你赢了：', debt)
        else:
            Next_f = True

print('你破惨了！！，gameover')
