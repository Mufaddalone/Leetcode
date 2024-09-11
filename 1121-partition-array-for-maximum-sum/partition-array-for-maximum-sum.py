class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*n
        def part(ind):
            if ind==n:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            lens = 0
            maxans = 0
            maxi = float("-inf")
            for j in range(ind,min(n,ind+k)):
                lens+=1
                maxi = max(maxi,arr[j])
                sum = (lens*maxi) + part(j+1)
                maxans = max(sum,maxans)
                dp[ind] = maxans
            return dp[ind]
        return part(0)
