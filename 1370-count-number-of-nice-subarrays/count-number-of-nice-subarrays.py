class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def notgoal(k):
            if k<0:return 0
            l=sums=count=0
            for r in range(len(nums)):
                sums += nums[r]%2
                while sums>k:
                    sums-=nums[l]%2
                    l+=1
                count += r-l+1
            return count
        ans = notgoal(k) - notgoal(k-1)
        return ans
        
                