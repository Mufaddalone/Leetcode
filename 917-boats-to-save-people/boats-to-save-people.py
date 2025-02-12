class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        count=0
        l,r = 0 ,len(nums)-1
        while l<=r:
            remain = limit-nums[r]
            r-=1
            count+=1
            if remain>=nums[l]:
                l+=1
        return count