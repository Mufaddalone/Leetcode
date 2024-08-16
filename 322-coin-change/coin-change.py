class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for j in range(amount+1)]for i in range(len(coins))]
        def f(ind,target):
            if ind ==0:
                if target %coins[ind] == 0:
                    return target//coins[ind]
                else:
                    return float("inf")
            if dp[ind][target]!=-1:
                return dp[ind][target]
            notpick = 0 + f(ind-1,target)
            take = float('inf')
            if coins[ind] <= target:
                take = 1 + f(ind,target - coins[ind])
            dp[ind][target] = min(take,notpick)
            return dp[ind][target]
        result = f(len(coins) - 1, amount)
        
        return result if result != float('inf') else -1