class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        ans = []

        def back(ind,arr):
            if len(arr) == len(digits):
                ans.append(arr)
                return 
            for i in key[digits[ind]]:
                back(ind+1,arr+i)
        if len(digits):
            back(0,"")
        return ans

            



