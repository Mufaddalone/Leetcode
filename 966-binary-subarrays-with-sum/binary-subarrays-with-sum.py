class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        def notgoal(nums,k):
            l = 0 
            sums= 0
            count = 0
            if k<0:return 0
            for r in range(len(nums)):
                sums += nums[r]
                while sums> k:
                    sums-=nums[l]
                    l+=1
                count += r-l+1
            return count
        ans = notgoal(nums,k) - notgoal(nums,k-1)
        return ans
                    
        