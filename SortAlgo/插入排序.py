# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/10/24 下午4:17

简单插入排序操作n-1轮，每轮将一个未排序树插入排好序列。
开始时默认第一个数有序，将剩余n-1个数逐个插入。插入操作具体包括：比较确定插入位置，数据移位腾出合适空位

'''
# 时间复杂度 O(N^2)
# 空间复杂度 O(1)


def InsertSort(arr):
    n = len(arr)
    if n<=1:
        return arr

    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j>=0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = curr

    return arr

arr = [2, 1, 5, 3, 8, 20, 6, 7]
print(InsertSort(arr))