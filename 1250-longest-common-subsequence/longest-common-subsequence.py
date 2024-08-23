class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        # Create a DP table of size (n+1) x (m+1) initialized with -1
        dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]

        # # dp = [[-1 for i in range(len(text2)+1)]for j in range(len(text1)+1)]
        # memo = {}
        # def f(ind1,ind2):
        #     if ind1<0 or ind2<0:
        #         return 0
        #     # if dp[ind1][ind2]!=-1:
        #     #     return dp[ind1][ind2]
        #     if (ind1,ind2) in memo:
        #         return memo[(ind1,ind2)]
        #     # if text1[ind1] == text2[ind2]:
        #     #     dp[ind1][ind2] = 1 + f(ind1-1,ind2-1)
        #     #     return dp[ind1][ind2]
        #     if text1[ind1] == text2[ind2]:
        #         memo [(ind1,ind2)] = 1 + f(ind1-1,ind2-1)
        #     # dp[ind1][ind2]= max(f(ind1-1,ind2),f(ind1,ind2-1))
        #     # return dp[ind1][ind2]
        #     else: memo[(ind1,ind2)]= max(f(ind1-1,ind2),f(ind1,ind2-1))
        #     return memo[(ind1,ind2)]
        # return f(len(text1)-1,len(text2)-1)