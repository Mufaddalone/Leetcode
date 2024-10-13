class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        q = deque()
        q.append((beginWord,1))
        # wordset.remove(beginWord)
        while q:
            word,dist = q.popleft()
            if word == endWord: return dist
            for i in range(len(word)):
                original = word[i]
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a') + j)
                    new_word = ''.join(word_list)
                    if new_word in wordset:
                        wordset.remove(new_word)
                        q.append((new_word, dist+1))    
                word_list[i] = original
        return 0
                    