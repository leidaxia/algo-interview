# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/10/24 上午10:23
'''
#时间复杂度 O(NlogN)
#空间复杂度 O(NlogN)
# 是一种分治算法

def QuickSort(arr, left, right):
    if left >= right:
        return
    mid = parition(arr, left, right)
    QuickSort(arr, left, mid-1)
    QuickSort(arr, mid+1, right)



def parition(arr, left, right):
    curr = left
    while left < right:
        while left < right and arr[right] >= arr[curr]:
            right -= 1
        while left < right and arr[left] <= curr:
            left += 1

        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[right] = arr[right], arr[left]
    return left



arr = [2, 1, 5, 3, 8, 20, 6, 7]
n = len(arr)
QuickSort(arr, 0, n-1)
print(arr)



