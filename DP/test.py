# print([] + [[1,2]] + [[3,4]])
n=8
grid = [['.'] * n for i in range(n)]
# print(grid)
aa =[]
# aa = aa.append(["".join(h) for h in grid])
# aa = aa.append(["".join(h) for h in grid])
aa += [["".join(h) for h in grid]]
aa += [["".join(h) for h in grid]]



print(aa)