class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m = len(board)
        n = len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or (r,c) in visited:
                return 
            if board[r][c] == "O":
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        # Traverse the first and last columns
        for i in range(m):
            if (i, 0) not in visited and board[i][0] == "O":
                dfs(i, 0)
            if (i, n - 1) not in visited and board[i][n - 1] == "O":
                dfs(i, n - 1)

        for j in range(n):
            if (0, j) not in visited and board[0][j] == "O":
                dfs(0, j)
            if (m - 1, j) not in visited and board[m - 1][j] == "O":
                dfs(m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if ((i,j) not in visited and board[i][j] == "O"):
                    board[i][j] = "X"
        
