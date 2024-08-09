class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j, dp):
                    count += 1

        return count

    def isPalindrome(self, s: str, start: int, end: int, dp: list) -> bool:
        if start >= end:
            return True

        if dp[start][end]:
            return dp[start][end]

        if s[start] == s[end]:
            dp[start][end] = self.isPalindrome(s, start + 1, end - 1, dp)
            return dp[start][end]

        dp[start][end] = False
        return dp[start][end]
