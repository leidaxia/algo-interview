
# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/10/24 上午10:25
'''


def bubbleSort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [2, 1, 5, 3, 8, 20, 6, 7]
print(bubbleSort(arr))


