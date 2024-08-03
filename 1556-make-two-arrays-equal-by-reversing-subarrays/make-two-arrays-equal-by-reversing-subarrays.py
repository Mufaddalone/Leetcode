class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = {}
        for i in arr:
            a[i] = a.get(i,0)+1
        for i in target:
            if i not in a or a[i] == 0:
                return False
            a[i] -=1
        return True