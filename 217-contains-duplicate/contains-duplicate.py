class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        z= set()
        for i in nums:
            if i in z:
                return True
            z.add(i)
        return False