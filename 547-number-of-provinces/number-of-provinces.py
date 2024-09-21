class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:
        visited = set()
        pro = 0
        def dfs(i):
            visited.add(i)
            for j in range(len(a)):
                if a[i][j] == 1 and j not in visited:
                    dfs(j)
                    
        for i in range(len(a)):
            if i not in visited:
                pro +=1
                dfs(i)
        return pro