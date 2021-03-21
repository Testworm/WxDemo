#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author : yangge.yw
# @Time : 2021/3/18 8:52 上午
# @File : case_2.py
# @desc :
if __name__ == "__main__":

    # 导入库
    from allpairspy import AllPairs

    # 列出所有参数
    parameters = [
        ["Ie", "Firefox", "Chrome", "UC", "QQ"],
        ["Ios10", "Ios11", "Ios12", "Ios13"],
        ["用例1", "用例2", "用例3", "用例4", "用例5"]
    ]

    # 输出 pairwise 参数组合
    if __name__ == '__main__':
        print("PAIRWISE:")
        for i, pairs in enumerate(AllPairs(parameters)):
            print("{:2d}: {}".format(i, pairs))
