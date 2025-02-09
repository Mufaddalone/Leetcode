class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r=m-1,n-1
        for i in range(len(nums1)-1,-1,-1):
            if l < 0:
                nums1[:i+1] = nums2[:r+1]
                break
            if r<0:
                break
            if nums1[l]>nums2[r]:
                nums1[i] = nums1[l]
                l-=1
            else:
                nums1[i] = nums2[r]
                r-=1
        return nums1
            