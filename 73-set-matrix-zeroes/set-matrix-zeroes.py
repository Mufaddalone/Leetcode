class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = len(matrix)
        visit = [row[:] for row in matrix]
        def zero(r,c):
            if visit[r][c] !=0:
                return 
            for i in range(m):
                matrix[i][c] = 0
            for j in range(n):
                matrix[r][j] = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero(r,c)
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