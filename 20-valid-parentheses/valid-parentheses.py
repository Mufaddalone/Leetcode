class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"]":"[","}":"{",")":"("}
        a = []

        for i in s:
            if i in closing:
                if a and closing[i]==a[-1]:
                    a.pop()
                else:
                    return False
            else:
                a.append(i)
        return True if not a else False
                


                
            