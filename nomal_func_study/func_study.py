import pandas as pd
import numpy as np
import requests
import json, os, sys, time
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
    pass


def lambda_study():
    # 简单举例:
    square1 = lambda x: x*x
    result = square1(5)
    print(result)

    # 将某个列表中所有元素都计算平方
    list1 = [1, 2, 3, 4, 5]
    square2 = list(map(lambda x: x*x, list1))
    print(square2)

    # 筛选出列表中的偶数：
    list_ou = list(filter(lambda x: x % 2 == 0, list1))
    print(list_ou)


if __name__ == '__main__':
    lambda_study()
    # map_study()