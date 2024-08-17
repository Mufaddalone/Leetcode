from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [[-1 for j in range(amount + 1)] for i in range(len(coins))]
        prev = [0]*(amount+1)
        curr = [0]*(amount+1)

        # Initialize the base case for the first row (only using the first coin)
        for i in range(amount + 1):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]
            else:
                prev[i] = int(1e9)  # Use a large number to represent infinity
        
        # Fill the dp table
        for ind in range(1, len(coins)):
            for target in range(amount + 1):
                notpick = prev[target]
                take = int(1e9)  # Initialize to a large number
                if coins[ind] <= target:
                    take = 1 + curr[target - coins[ind]]
                curr[target] = min(take, notpick)
            prev = curr
        
        result = prev[amount]
        return result if result != int(1e9) else -1


        # dp = [math.inf] * (amount+1)
        # dp[0] = 0

        # for a in range(1,amount+1):
        #     for coin in coins:
        #         if coin <= a:
        #             dp[a] = min(dp[a],1+ dp[a-coin])
        
        # If dp[amount] is still infinity, it means we can't form that amount with the given coins
        
        # return dp[amount] if dp[amount] != math.inf else -1
        # dp = [[-1 for j in range(amount+1)]for i in range(len(coins))]
        # def f(ind,target):
        #     if ind ==0:
        #         if target %coins[ind] == 0:
        #             return target//coins[ind]
        #         else:
        #             return float("inf")
        #     if dp[ind][target]!=-1:
        #         return dp[ind][target]
        #     notpick = 0 + f(ind-1,target)
        #     take = float('inf')
        #     if coins[ind] <= target:
        #         take = 1 + f(ind,target - coins[ind])
        #     dp[ind][target] = min(take,notpick)
        #     return dp[ind][target]
        # result = f(len(coins) - 1, amount)
        
        # return result if result != float('inf') else -1