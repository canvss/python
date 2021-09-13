# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/28 22:34
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
def main():
    with open('基础1-15/node', 'r', encoding='utf-8') as f:
        print(f.read())


def test_file():
    op = None
    # 获取写的对象
    # op_write = open('test_file','w',encoding='utf-8')
    # op_write.write('hello')
    try:
        op = open('tet_file','r',encoding='utf-8')
        print(op.read())
    except FileNotFoundError:
        print('文件找不到')
    finally:
        try:
             op.close()
        except:
            print('NoneType')

if __name__ == '__main__':
    # main()
    test_file()