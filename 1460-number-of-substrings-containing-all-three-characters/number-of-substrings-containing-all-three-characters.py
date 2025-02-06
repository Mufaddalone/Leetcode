class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen = {"a":-1,"b":-1,"c":-1}
        count = 0
        for i in range(len(s)):
            lastseen[s[i]] = i
            count = count + (1+min(lastseen["a"],lastseen["b"],lastseen["c"]))
        return count