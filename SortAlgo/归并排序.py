# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/10/24 上午10:26
'''


def MergeSort(arr):

    def merge(arr, left, mid, right):
        i = left
        j = mid + 1
        temp = []
        while i<=mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i = i+1
            else:
                temp.append(arr[j])
                j = j+1

        while i<=mid:
            temp.append(arr[i])
            i = i+1
        while j<=right:
            temp.append(arr[j])
            j = j+1

        for i in range(left, right+1):
            arr[i] = temp[i-left]


    def mergeAndPartition(arr, left, right):
        # 回溯法都有一个回溯终止的条件, 相当于减枝, 很重要！！！！！！
        if left >= right:
            return
        mid = (left + right) // 2
        mergeAndPartition(arr, left, mid)
        mergeAndPartition(arr, mid+1, right)
        merge(arr, left, mid, right)


    n = len(arr)
    mergeAndPartition(arr, 0, n-1)

    return arr

arr = [2, 1, 5, 3, 8, 20, 6, 7]
print(MergeSort(arr))


