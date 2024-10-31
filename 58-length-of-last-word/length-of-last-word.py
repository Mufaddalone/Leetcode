class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.split()
        if not b:
            return 0
        return len(b[-1])
