class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n^res
        return res
        # s = {}
        # for i in nums:
        #     s[i] = s.get(i,0)+1
        # for i,j in s.items():
        #     if j==1:
        #         return i