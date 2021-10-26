# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/10/24 上午10:26
'''
# 大顶堆指任意一个父节点都不小于左右两个孩子节点的完全二叉树，根节点最大

# n是数组arr的元素大小, i是从哪个点开始进行heapify, 从上到下开始
def heapify(arr, n, i):
    #左子节点
    c1 = 2*i + 1
    #右子节点
    c2 = 2*i + 2
    max = i

    if (c1 < n and arr[c1] > arr[max]):
        max = c1

    if (c2 < n and arr[c2] > arr[max]):
        max = c2

    if max != i:
        arr[max], arr[i] = arr[i], arr[max]
        heapify(arr, n, max)

def build_heap(arr, n):
    last_node = n-1
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr, n):
    build_heap(arr, n)
    for i in range(n-1, -1 , -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


arr = [2, 1, 5, 3, 8, 20, 6, 7]
print(heap_sort(arr, 8))















