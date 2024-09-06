class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        
        words.sort(key=len)
        word_set = set(words)
        dp = {}
        
        def is_predecessor(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            i = j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    i += 1
                j += 1
            return i == len(word1)
        
        max_chain = 1
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in word_set:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain = max(max_chain, dp[word])
        
        return max_chain