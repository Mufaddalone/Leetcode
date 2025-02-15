class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l= 0
        z = set()
        for r in range(len(nums)):
            if r-l > k:
                z.remove(nums[l])
                l+=1
            if nums[r] in z:
                return True
            z.add(nums[r])
        return False
                