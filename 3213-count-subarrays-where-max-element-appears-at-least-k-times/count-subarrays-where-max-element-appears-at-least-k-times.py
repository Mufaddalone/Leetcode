class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        l = 0
        count = 0
        ans =0
        for r in range(len(nums)):
            if nums[r] == maxi:
                count+=1
            while count>=k:
                if nums[l] == maxi:
                    count-=1
                l+=1
            ans += l
        return ans

                