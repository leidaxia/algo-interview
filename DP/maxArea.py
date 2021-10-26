# -*- coding: utf-8 -*
'''
@author: leiming
@time: 2021/9/20 8:59 下午
'''
import time

def maximalRectangle(matrix) -> int:
    # https://www.bilibili.com/video/BV1Dk4y127j4?spm_id_from=333.999.0.0
    row = len(matrix)
    column = len(matrix[0])

    dp = [[0] * (column) for _ in range(row)]
    print(dp)

    area = 0

    for i in range(row):
        for j in range(column):
            if matrix[i][j] == "1":
                dp[i][j] = 1

    for i in range(1, row):
        for j in range(column):
            if dp[i - 1][j] >= 1:
                if dp[i][j] == 1:
                    dp[i][j] = dp[i - 1][j] + 1

    print(dp)

    for i in range(row):
        for j in range(column):
            print(f"i:{i}, j:{j}")
            if dp[i][j] == 0: continue
            curHeight = dp[i][j]
            print(f"curHeight:{curHeight}")
            for k in range(j, -1, -1):
                if dp[i][k] == 0: break
                print(f"k:{k}")
                curWeigth = j - k + 1
                print(f"curWeigth:{curWeigth}")
                curHeight = min(dp[i][k], curHeight)
                print(f"curHeight:{curHeight}")

                area = max(area, dp[i][k], curWeigth * curHeight)
                print(f"area:{area}")

            print("///////////////////////////////////////////////////////////////")
            time.sleep(1)

    return area


if __name__ == "__main__":
    input = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    print(maximalRectangle(input))