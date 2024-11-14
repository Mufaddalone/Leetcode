class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                l,r = j+1,len(nums)-1
                while l<r:
                    four = nums[l]+nums[r]+nums[i]+nums[j]
                    if four<target:
                        l+=1
                    elif four>target:
                        r-=1
                    else:
                        res.append([nums[l],nums[r],nums[i],nums[j]])
                        l+=1
                        r-=1
                        while l<r and nums[l] ==nums[l-1]:
                            l+=1
                        while r>l and  nums[r] == nums[r+1]:
                            r-=1
        return res