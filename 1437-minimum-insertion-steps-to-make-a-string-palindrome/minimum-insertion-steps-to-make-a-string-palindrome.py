class Solution:
    def minInsertions(self, s: str) -> int:
        def pal(t1,t2):
            n,m = len(t1),len(t2)
            dp = [[0 for j in range(m+1)]for i in range(n+1)]

            for i in range(1,n+1):
                for j in range(1,m+1):
                    if t1[i-1] == t2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[n][m]
        return len(s) - pal(s,s[::-1])