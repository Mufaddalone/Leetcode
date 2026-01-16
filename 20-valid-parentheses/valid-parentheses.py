class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"}":"{","]":"[",")":"("}
        a = []
        for i in s:
            if i in closing:
                if a and a[-1] == closing[i]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        return len(a)==0