class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suf =1,1
        maxi = float("-inf")
        for i in range(len(nums)):
            if pre == 0:
                pre =1
            if suf == 0:
                suf =1
            pre = pre * nums[i]
            suf = suf * nums[len(nums)-i-1]
            maxi = max(maxi, max(pre,suf))
        return maxi