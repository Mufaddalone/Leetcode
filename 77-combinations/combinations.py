class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        ans = []

        def back(ind):
            if len(arr) == k:
                ans.append(arr[:])
                return
            for i in range(ind,n+1):
                arr.append(i)
                back(i+1)
                arr.pop()
        back(1)
        return ans

                

        