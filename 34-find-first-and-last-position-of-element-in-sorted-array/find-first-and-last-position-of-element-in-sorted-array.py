class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            l, r = 0, len(nums) - 1
            first = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    first = mid
                    r = mid - 1  # Continue searching to the left
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return first

        def findLast(nums, target):
            l, r = 0, len(nums) - 1
            last = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    last = mid
                    l = mid + 1  # Continue searching to the right
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return last

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]