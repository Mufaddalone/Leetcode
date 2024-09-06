class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def compare(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            i = j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    i += 1
                j += 1
            return i == len(word1)

        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        max_len = 1

        for i in range(1, n):
            for j in range(i):
                if compare(words[j], words[i]) and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            max_len = max(max_len, dp[i])

        return max_len