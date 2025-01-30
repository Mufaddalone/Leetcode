class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums1indx = {n: i for i, n in enumerate(nums2)}
        print(nums1indx)
        arr = [-1]*len(nums2)
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i]>=stack[-1]:
                stack.pop()
            if not stack: arr[i] = -1
            else: arr[i] = stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = arr[nums1indx[nums1[i]]]
        return nums1
        # for i in range(len(nums1)):
        #     nums1[i] = nums1indx[nums2[i]]
        # return nums1[1]
        