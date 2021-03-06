# -*- coding:utf-8 -*-

from numpy import *
import operator


# 通过KNN进行分类
def classify(test, train, label, k):
    data_size = train.shape[0]  # row is 4.
    diff = tile(test, (data_size, 1)) - train  # 计算欧式距离
    sq_diff = diff ** 2
    sq_dist = sum(sq_diff, axis=1)  # 行向量分别相加，从而得到新的一个行向量
    dist = sq_dist ** 0.5

    # 对距离进行排序
    sort_dist = argsort(dist)  # argsort()根据元素的值从大到小对元素进行排序，返回下标

    # 对选取的K个样本所属的类别个数进行统计
    class_count = {}
    for i in range(k):
        vote_label = label[sort_dist[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "Classified"
    return sorted_class_count[0][0]

    # 选取出现的类别次数最多的类别
    # max_count = 0
    # for key, value in class_count.items():
    #     if value > max_count:
    #         max_count = value
    #         classes = key
    # return classes

