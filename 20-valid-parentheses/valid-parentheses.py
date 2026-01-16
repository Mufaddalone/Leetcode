class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"}":"{","]":"[",")":"("}
        a = []
        for i in s:
            if i in closing and len(a)!=0:
                if a[-1] == closing[i]:
                    a.pop()
                else:
                    return False
            elif i in closing:
                return False
            else:
                a.append(i)
        return len(a)==0