# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/2/20 11:25 下午
'''

s = ")()())"

window = "()"
n = len(s)
res = 0

for i in range(1, n):
    if s[i - 1:i + 1] == window:
        left = i - 1
        right = i

        while (left - 2) >= 0 and s[left - 2:left] == window:
            left = left - 2

        while (right + 3) <= n and s[right + 1:right + 3] == window:
            right = right + 2

        res += right - left + 1

print(res)
