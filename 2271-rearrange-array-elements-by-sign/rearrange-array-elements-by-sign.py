class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = r = 0
        res =[]
        for i in range(len(nums)):
            if i%2 ==0:
                while l<len(nums) and nums[l]<0:
                    l+=1
                res.append(nums[l])
                l+=1
            else:
                while r<len(nums) and nums[r]>=0:
                    r+=1
                res.append(nums[r])
                r+=1      
        return res