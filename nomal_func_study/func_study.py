import pandas as pd
import numpy as np
import requests
import json, os, sys, time, random
from datetime import datetime, timedelta


def map_study():
    """
    map函数：第一个元素为需要调用的函数名，后面的参数根据此函数要求的参数数量来传，接受一个或多个可迭代的序列，
    然后【把函数依次作用在序列的【每一个元素上】】，并构造一个新的list返回，不影响原list
    """
    def s(x):
        return x*x
    list1 = [1, 2, 3, 4, 5]
    map_s = map(s, list1)
    print(list(map_s))

    def add(x, y):
        return x + y
    list2 = [1, 1, 1, 1, 10]
    map_add = map(add, list1, list2)
    print(list(map_add))


def filter_study():
    """
    filter 函数用于过滤出满足第一个参数【函数】的列表元素
    """
    list1 = [1, 2, 3, 4, 5]
    list1_modify = map(lambda x: x*x, list1)
    print(list(list1_modify))

    # 过滤掉列表中所有的偶数：
    list1_ou = filter(lambda x: x % 2 == 0, list1)
    print(list(list1_ou))


def lambda_study():
    # 简单举例:
    square1 = lambda x: x*x
    result = square1(5)
    print(result)

    # 将某个列表中所有元素都计算平方
    list1 = [1, 2, 3, 4, 5]
    square2 = list(map(lambda x: x*x, list1))
    print(square2)

    # 筛选出列表中的偶数, filter函数用于过滤：
    list_ou = list(filter(lambda x: x % 2 == 0, list1))
    print(list_ou)


# pandas 的 apply方法学习
def dataframe_apply_study():
    # 构建一个基础dataframe：
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }, index=['a', 'b', 'c'])
    # print(df)

    # 对每一行求和后返回新的df
    """
    axis = 0，表示按列处理
    axis = 1，表示按行处理
    """
    df1 = df.apply(lambda x: sum(x), axis=0)
    # print(df1)

    # 进阶操作，先生成一个10*5的随机数矩阵, 如果第五列的值大于0.5时，那么新生成的第六列等于第1,3列的和，否则等于第二列：
    df_random = pd.DataFrame(np.random.random((10, 5)))
    print(df_random)
    df_random['special'] = df_random.apply(lambda x: x[0] + x[2] if x[4] > 0.5 else x[1], axis=1)
    print(df_random)


if __name__ == '__main__':
    # lambda_study()
    # map_study()
    # filter_study()
    dataframe_apply_study()