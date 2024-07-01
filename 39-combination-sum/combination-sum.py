class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        ans = []

        def back(ind , target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(arr[:])
                return
            if candidates[ind]<=target:
                arr.append(candidates[ind])
                back(ind,target-candidates[ind])
                arr.pop()
            back(ind+1, target)
        back(0,target)
        return ans
