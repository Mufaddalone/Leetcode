class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest =0
        numset = set(nums)
        for i in numset:
            if i-1 not in numset:
                length = 1
                while i+length in numset:
                    length += 1
                longest = max(longest ,length)
        return longest
        # nums.sort()
        # temp =0
        # count = 0
        # if len(nums) ==0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]-1:
        #         temp +=1
        #     else:
        #         temp=0
        #     if temp>= count:
        #         count=temp
        # return count+1