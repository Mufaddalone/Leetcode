class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            cost = prices[i] - mini
            profit = max(cost, profit)
            mini = min (mini,prices[i])
        return profit
        # l,r = 0,1
        # maxp = 0
        # while r<len(prices):
        #     profit = prices[r]-prices[l]
        #     if prices[r]>prices[l]:
        #         maxp = max(profit,maxp)
        #     else:
        #         l=r
        #     r+=1
        # return maxp

        # maxp =0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j] - prices[i]
        #         maxp = max(maxp, profit)
        # return maxp

            

        