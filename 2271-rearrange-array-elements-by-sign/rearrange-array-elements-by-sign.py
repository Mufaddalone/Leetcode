class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l1 =[]
        l2 = []
        l3 = []
        for i in nums:
            if i>0:
                l1.append(i)
            else:
                l2.append(i)
        for i in range(len(l1)):
            l3.append(l1[i])
            l3.append(l2[i])
        return l3
        # l = r = 0
        # res =[]
        # for i in range(len(nums)):
        #     if i%2==0:
        #         while r< len(nums) and nums[r]<0:
        #             r+=1
        #         res.append(nums[r])
        #         r+=1
        #     else:
        #         while l<len(nums) and nums[l]>0:
        #             l+=1
        #         res.append(nums[l])
        #         l+=1
        # return res


