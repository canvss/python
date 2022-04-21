# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/19 22:25

'''
    文件修改
'''

import os


with open('user.txt', mode='rt', encoding='utf-8')as rf,\
    open('.user.txt.swap', mode = 'wt', encoding='utf-8')as wf:
    for line in rf:
        wf.write(line.replace('jack','tom'))

os.remove('user.txt')
os.rename('.user.txt.swap','user.txt')