class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)

        for i in s:
            a[i] += 1

        for j in t:
            a[j] -=1

        for i in a.values():
            if i!=0:
                return False
        return True

