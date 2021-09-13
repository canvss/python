# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/5/28 23:16
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
# 通过读取二进制复制图片
def main():
    mfs = None
    try:
        with open('基础1-15/img.png', mode='rb') as mf:
            mfs = mf.read()
        with open('基础1-15/copy_img.png', mode='wb') as wf:
            wf.write(mfs)
    except FileNotFoundError:
        print('文件不存在')
    except IOError:
        print('文件写入出错')
if __name__ == '__main__':
    main()