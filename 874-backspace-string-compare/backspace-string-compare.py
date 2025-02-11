class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        for i in s:
            if a and i =="#":
                a.pop()
            elif i!="#":
                a.append(i)
        for i in t:
            if b and i =="#":
                b.pop()
            elif i!="#":
                b.append(i)
                print(b)
        return a==b
        