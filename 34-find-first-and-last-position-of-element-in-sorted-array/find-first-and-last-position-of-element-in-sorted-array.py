class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstele():
            l,r = 0, len(nums)-1
            first = -1
            while l<=r:
                mid = (r+l)//2
                if nums[mid] == target:
                    first = mid
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r=mid-1
            return first
        def lastele():
            l,r = 0, len(nums)-1
            last =-1
            while l<=r:
                mid = (r+l)//2
                if nums[mid] == target:
                    last = mid
                    l = mid+1
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r=mid -1
            return last
        
        return [firstele(),lastele()]