class Solution:
    def findMin(self, nums: List[int]) -> int:
        low , high = 0, len(nums)-1
        while low<high:
            mid = low + (high-low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[l]<nums[r]:
        #         r =mid-1
        #         res= min(res,nums[mid])
        #     else:
        #         l = mid+1
        #         res = min (res,nums[mid])
        # return res



















        # res = nums[0]
        # l,r = 0, len(nums)-1
        # while l<=r:
        #     if nums[l] < nums[r]:
        #         res = min(res,nums[l])
        #         break

        #     mid = (l+r)//2
        #     res = min(nums[mid],res)
        #     if nums[mid] >= nums[l]:
        #         l = mid+1
        #     else:
        #         r = mid-1
        # return res


            # for i in range(len(nums)-1):
            #     if nums[i] > nums[i+1]:
            #         return nums[i+1]
            # return nums[0]
            # low , high = 0, len(nums)-1
            # while low<high:
            #     mid = low + (high-low)//2
            #     if nums[mid] > nums[high]:
            #         low = mid + 1
            #     else:
            #         high = mid
            # return nums[low]

        