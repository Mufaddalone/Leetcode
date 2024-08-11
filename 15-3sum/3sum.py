class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                threesum = nums[l]+nums[r]+a
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([nums[l],nums[r],a])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
        return res

        # res = []
        # x= 0
        # for k in range(1,len(nums)-1):
        #     l = k+1
        #     if nums[x] + nums[k]+ nums[l] == 0 and x!=l!=k:
        #         if [nums[x],nums[k],nums[l]] in res:
        #             continue
        #         res.append([nums[x], nums[k], nums[l]])
        # return res
                    

        