class Solution:
    def maxLength(self, arr: List[str]) -> int:
        seen = set()
        def check(st):
            _seen = set()
            for c in st:
                if c in seen or c in _seen:
                    return True
                _seen.add(c)
            return False
        def dp(i):
            if i == len(arr):
                return len(seen)
            res = 0
            if not check(arr[i]):
                for ch in arr[i]:
                    seen.add(ch)
                res = dp(i+1)
                for ch in arr[i]:
                    seen.remove(ch)
            return max(res,dp(i+1))
        
        return dp(0)