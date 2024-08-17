class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def f(ind: int, total: int) -> int:
            if ind == len(nums):
                return 1 if total == target else 0

            if (ind,total) in dp:
                return dp[(ind, total)]
            
            # Consider both adding and subtracting the current element.
            add = f(ind + 1, total - nums[ind])
            subtract = f(ind + 1, total + nums[ind])
            
            dp[(ind, total)]  = add + subtract
            return dp[(ind, total)]
        
        return f(0, 0)