class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        table = [0]*(amount+1)
        table[0] = 1

        for i in range(n-1, -1, -1):
            for j in range(coins[i], amount + 1):
                table[j] += table[j - coins[i]]
        
        return table[amount]
        # dp = [[-1 for i in range(amount+1)]for j in range(len(coins))]
        # def f(ind,target):
        #     if target == 0:
        #         return 1
        #     if ind < 0:
        #         return 0
        #     if dp[ind][target]!= -1:
        #         return dp[ind][target]
        #     nottake = f(ind-1, target)
        #     take = 0
        #     if coins[ind] <= target:
        #         take = f(ind,target-coins[ind])
        #     dp[ind][target] = take + nottake
        #     return dp[ind][target]
        # return f(len(coins)-1,amount)
