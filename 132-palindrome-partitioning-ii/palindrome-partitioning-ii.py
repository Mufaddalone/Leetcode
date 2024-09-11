class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [-1]*n
        def part(i):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            temp = ""
            mini = float("inf")
            for j in range(i,n):
                temp+=s[j]
                if isPal(temp):
                    cost = 1+part(j+1)
                    mini = min(mini,cost)
                    dp[i] = mini
            return dp[i]
        def isPal(s):
            return s==s[::-1]
            # m = len(s)
            # for i in range(m//2):
            #     if s[i] != s[m-i-1]:
            #         return False
            # return True
        return part(0)-1
        