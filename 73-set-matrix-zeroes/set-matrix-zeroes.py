class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rowzero = False

        # First pass: mark zeros on the first row and first column
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True

        # Second pass: use marks to set elements to zero
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Set the first column to zero if needed
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        # Set the first row to zero if `rowzero` is True
        if rowzero:
            for c in range(n):
                matrix[0][c] = 0



        # a = set()
        # b = set()
        # for i in range(m):
        #     for j in range(n):
        #         if(matrix[i][j]==0):
        #             a.add(i)
        #             b.add(j)
        
        # for i in a:
        #     matrix[i] = [0]*n
        
        # for j in b:
        #     for i in range(m): matrix[i][j]=0
        # n = len(matrix[0])
        # m = len(matrix)
        # row = [0]*m
        # col = [0]*n
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] ==0:
        #             row[i] = 1
        #             col [j] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if row[i] ==1 or col[j] ==1:
        #             matrix[i][j] =0
                

        # n = len(matrix[0])
        # m = len(matrix)
        # visit = [row[:] for row in matrix]
        # def zero(r,c):
        #     if visit[r][c] !=0:
        #         return 
        #     for i in range(m):
        #         matrix[i][c] = 0
        #     for j in range(n):
        #         matrix[r][j] = 0
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c] == 0:
        #             zero(r,c)
        # n = len(matrix[0])
        # m = len(matrix)
        # dri = [[0,1],[1,0],[-1,0],[0,-1]]
        # visited = [[0 for j in range(n)]for i in range(m)]
        # def dfs(r,c):
        #     matrix[r][c] = 0
        #     visited[r][c] = 1
        #     for dr, dc in dri:
        #         nr,nc = dr+r,dc+c
        #         if 0<=nr<m and 0<=nc<n and visited[nr][nc] == 0:
        #             dfs(nr,nc)
        # for r in range(m):
        #     for c in range(n):
        #         if matrix[r][c] == 0:
        #             dfs(r,c)