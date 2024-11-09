class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf") # maximum sum
        sum = 0

        for i in nums:
            sum += i
            maxi = max(sum,maxi)
            if sum < 0:
                sum = 0
        return maxi
            

            