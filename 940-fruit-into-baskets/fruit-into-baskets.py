class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        z = defaultdict(int)
        l= 0 
        count =0
        for r in range(len(fruits)):
            z[fruits[r]]+=1
            while len(z) >2:
                z[fruits[l]]-=1
                if z[fruits[l]]==0:
                    del z[fruits[l]]
                l+=1
            count = max(count,r-l+1)
        return count