class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j=0
        # for i in nums:
        #     if i != 0:
        #         nums[j] = i
        #         j+=1
        # for i in range(j,len(nums)):
        #     nums[i] = 0
        # return nums

        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
        return nums

                
        