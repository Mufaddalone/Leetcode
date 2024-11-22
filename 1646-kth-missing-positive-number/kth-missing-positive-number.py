class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # l,r = k,max(arr)+k
        # while l<=r:
        #     mid = (l+r)//2
        res = []
        z = set(arr)
        for i in range(max(arr)+k+1):
            if i not in z:
                res.append(i)
        return res[k]


        