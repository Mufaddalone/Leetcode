class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in strs:
            sort = "".join(sorted(i))
            a[sort].append(i)
        return a.values()


                

                        