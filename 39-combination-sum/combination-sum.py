class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        ans =[]
        ind = 0

        def backtracking(ind,target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(arr[:])
                return
            if candidates[ind] <= target:
                arr.append(candidates[ind])
                backtracking(ind,target-candidates[ind])
                arr.remove(candidates[ind])
            backtracking(ind+1,target)
        backtracking(0,target)
        return ans


        
        