class Solution:
    def solveNQueens(self, n):

        grid = [['.'] * n for i in range(n)]

        # 记录Q出现的索引
        queen = set()

        output = []
        # print(grid)


        self.queenDFS(grid, 0, n,queen,output)

        return output






    def isQueenOk(self,grid,row,col):

        #纵向合法性校验
        for i in range(row):

            if grid[i][col] == 'Q':

                return False

        #主对角线合法性校验
        x = row - 1
        y = col - 1


        while x >= 0 and y >= 0:

            if grid[x][y] == 'Q':

                return False
            x -= 1
            y -= 1


        #副对角线合法性校验
        x = row - 1
        y = col + 1



        while x >= 0 and y < len(grid[0]):

            if grid[x][y] == 'Q':

                return False
            x -= 1
            y += 1


        return True


    def queenDFS(self,grid,row,n,queen,output):

        if row == n:
            solution = []
            for _, col in sorted(queen):

                solution.append('.' * col + 'Q' + '.' * (n-col-1))

            output.append(solution)



        for i in range(n):

            if(self.isQueenOk(grid,row,i)):
                # print("####")

                queen.add((row,i))

                grid[row][i] = 'Q'


                self.queenDFS(grid, row + 1, n,queen,output)

                grid[row][i] = '.'
                queen.remove((row,i))