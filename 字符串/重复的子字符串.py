# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/2/19 10:23 下午
'''

s = "ababcbc"
n = len(s)
window = []

flag = True

for i in range(n):
    if s[i] not in window:
        window.append(s[i])
    else:
        break

print(window)
m = len(window)


if n % m != 0:
    flag = False

for i in range(m):
    print (f"i : {i}" )
    for j in range(i, n, m):
        print(f"j : {j}")
        if s[j] != window[i]:
            flag = False

print(flag)

print(s[0:1])

