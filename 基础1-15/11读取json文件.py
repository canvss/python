# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/28 23:33
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
import json


def main():
    # json文件
    mydict = {
        'name':'endless',
        'age':23,
        'qq':6858247,
        'friends':['jake','tom'],
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        # 写入json文件中
        with open('data.json','w',encoding='utf-8') as fj:
           #  序列化
           json.dump(mydict,fj)
    except IOError as e:
        print(e)
    print('over!!!')

def w_json():
    try:
        # 读取json
        with open('data.json',mode = 'r',encoding='utf-8') as rf:
            # 反序列化
            print(json.load(rf))
    except IOError as e:
        print(e)

if __name__ == '__main__':
    # main()
    w_json()