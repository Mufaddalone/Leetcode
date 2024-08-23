class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for i in range(len(text2)+1)]for j in range(len(text1)+1)]
        def f(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1] == text2[ind2]:
                dp[ind1][ind2] = 1 + f(ind1-1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2]= max(f(ind1-1,ind2),f(ind1,ind2-1))
            return dp[ind1][ind2]
        return f(len(text1)-1,len(text2)-1)