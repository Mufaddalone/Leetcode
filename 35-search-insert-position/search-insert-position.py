class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        ans = -1
        while l<=r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= target:
                ans = mid
                l+=1
            else:
                r-=1
        return ans+1