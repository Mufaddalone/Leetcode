class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for ind in range(n,-1,-1):
            lens = 0
            maxans = 0
            maxi = float("-inf")
            for j in range(ind,min(n,ind+k)):
                lens+=1
                maxi = max(maxi,arr[j])
                sum = (lens*maxi) + dp[j+1]
                maxans = max(sum,maxans)
                dp[ind] = maxans
        return dp[0]
        # n = len(arr)
        # dp = [-1]*n
        # def part(ind):
        #     if ind==n:
        #         return 0
        #     if dp[ind]!=-1:
        #         return dp[ind]
        #     lens = 0
        #     maxans = 0
        #     maxi = float("-inf")
        #     for j in range(ind,min(n,ind+k)):
        #         lens+=1
        #         maxi = max(maxi,arr[j])
        #         sum = (lens*maxi) + part(j+1)
        #         maxans = max(sum,maxans)
        #         dp[ind] = maxans
        #     return dp[ind]
        # return part(0)
