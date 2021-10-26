# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/10/10 上午11:43
'''

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

def dfs(grid, r, c):
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return
    if grid[r][c] != 1:
        return

    grid[r][c] = 2

    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)


res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            print(f"grid:{grid}")
            dfs(grid, i, j)
            res += 1
            print(f"res:{res}")


print(res)

