# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/2/22 11:05 下午
'''
s = "abcabcbb"
left = right = 0
window = {}
res = 0
n = len(s)

while right < n:
    c1 = s[right]
    if c1 not in window:
        window[c1] = 1
    else:
        window[c1] = window[c1] + 1

    right = right + 1

    while window[c1] > 1:
        c2 = s[left]
        window[c2] = window[c2] - 1
        left = left + 1

    res = max(res, right - left)
    print(res)