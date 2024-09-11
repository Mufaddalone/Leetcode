class Solution:
    def maxSumAfterPartitioning(self, num: List[int], k: int) -> int:
        n = len(num)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(i, k) + 1):
                max_val = max(max_val, num[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        return dp[n]
        # n = len(arr)
        # maxans = 0
        # def part(ind):
        #     if ind==n:
        #         return 0
        #     lens = 0
        #     maxi = float("-inf")
        #     for j in range(ind,min(n,k)):
        #         lens+=1
        #         maxi = max(maxi,arr[j])
        #         sum = (lens*maxi) + part(j+1)
        #         maxans = max(sum,maxans)
        #     return maxans
        # return part(0)
