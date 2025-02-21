class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
        def atmostk(k):
            l=0
            z = defaultdict(int)
            count = 0
            for r in range(len(s)):
                z[s[r]]+=1
                while len(z)>k:
                    z[s[l]]-=1
                    if z[s[l]] == 0:
                        del z[s[l]]
                    l+=1
                count+=r-l+1
            return count
        ans = atmostk(k) - atmostk(k-1)
        return ans
                        