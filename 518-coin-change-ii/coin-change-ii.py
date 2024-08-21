class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for i in range(amount+1)]for j in range(len(coins))]
        def f(ind,target):
            if target == 0:
                return 1
            if ind < 0:
                return 0
            if dp[ind][target]!= -1:
                return dp[ind][target]
            nottake = f(ind-1, target)
            take = 0
            if coins[ind] <= target:
                take = f(ind,target-coins[ind])
            dp[ind][target] = take + nottake
            return dp[ind][target]
        return f(len(coins)-1,amount)
