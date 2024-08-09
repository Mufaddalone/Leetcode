class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        # dp =[[-1 for i in range(m)]for j in range(n)]
        prev = [0]*m
        curr = [0]*m
        for i in range(m):
            prev[i] = matrix[0][i]
        for i in range(1,n):
            for j in range(m):
                up = matrix[i][j] + prev[j]
            
                # Handle left diagonal
                left_diagonal = matrix[i][j]
                if j - 1 >= 0:
                    left_diagonal += prev[j - 1]
                else:
                    left_diagonal += int(1e9)  # A large negative value if out of bounds
                
                # Handle right diagonal
                right_diagonal = matrix[i][j]
                if j + 1 < m:
                    right_diagonal += prev[j + 1]
                else:
                    right_diagonal += int(1e9)  # A large negative value if out of bounds
                
                # Store the maximum of the three moves in dp
                curr[j] = min(up, left_diagonal, right_diagonal)
            prev = curr[:]
        maxi = prev[n-1]
        for j in range(m):
            maxi = min(maxi,prev[j])
        return maxi
        # def f(i,j):
        #     if (j<0 or j>=m):
        #         return 1e9
        #     if i==0:
        #         return matrix[0][j]
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up = matrix[i][j] + f(i-1,j)
        #     left = matrix[i][j] + f(i-1,j-1)
        #     right = matrix[i][j] + f(i-1,j+1)
        #     dp[i][j] = min(up,left,right)
        #     return dp[i][j]

        # n =len(matrix)
        # m = len(matrix[0])
        # dp = [[-1 for i in range(m)]for j in range(n)]
        # maxi = 1e9
        # for j in range(m):
        #     maxi = min(maxi, f(m-1,j))
        # return maxi
