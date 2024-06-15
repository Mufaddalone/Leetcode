class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(2):
            for j in nums:
                a.append(j)
        return a