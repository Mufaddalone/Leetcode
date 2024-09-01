class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        a=[]
        if len(original)!=m*n:
            return[]
        for i in range(m):
            a.append(original[i*n:(i+1)*n])
        return a
