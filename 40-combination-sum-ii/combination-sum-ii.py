class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            arr = []
            ans = []
            cand = sorted(candidates)
            def backtracking(ind,target):
                if target == 0:
                    ans.append(arr[:])
                    return
                for i in range(ind ,len(cand)):
                    if i > ind and cand[i] == cand[i-1]: continue
                    if cand[i] > target: break
                    arr.append(cand[i])
                    backtracking(i+1, target- cand[i])
                    arr.pop()
            backtracking(0,target)
            return ans

