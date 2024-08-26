class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        '''
        Take smaller string 
        and find most common occurences???
        '''
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[0][0]

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