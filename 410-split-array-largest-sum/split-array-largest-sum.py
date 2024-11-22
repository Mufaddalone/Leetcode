class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def spliter(split):
            count = 1
            sums = 0
            for i in range(len(nums)):
                if nums[i] + sums <= split:
                    sums+= nums[i]
                else:
                    count+=1
                    sums = nums[i]
            return count
        l,r = max(nums),sum(nums)
        while l<=r:
            mid = (l+r)//2
            if spliter(mid) >k:
                l = mid+1
            else:
                r = mid-1
        return l