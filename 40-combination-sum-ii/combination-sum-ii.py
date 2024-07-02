class Solution:
    def combinationSum2(self, candidate: List[int], target: int) -> List[List[int]]:
        arr = []
        ans = []
        candidate.sort()
        def back(ind,target):
            if target ==0:
                ans.append(arr[:])
                return 
            for i in range(ind,len(candidate)):
                if i!=ind and candidate[i] == candidate[i-1]:continue
                if candidate[i]>target: break
                arr.append(candidate[i])
                back(i+1,target-candidate[i])
                arr.pop()
        back(0,target)
        return ans

        

