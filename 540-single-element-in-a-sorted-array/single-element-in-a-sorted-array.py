class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if nums[n-1]!= nums[n-2]:
            return nums[n-1]
        if nums[0]!= nums[1]:
            return nums[0]
        l,r=1,n-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid-1]!=nums[mid] and nums[mid+1]!=nums[mid]:
                return nums[mid]
            if mid%2==1 and nums[mid] == nums[mid-1] or mid%2==0 and nums[mid] == nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        
        