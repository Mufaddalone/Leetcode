class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:
        visited = [False] * len(a)
        pro = 0

        def dfs(i):
            visited[i] = True
            for j in range(len(a)):
                if a[i][j]==1 and visited[j] == False:
                    dfs(j)
                
        for i in range(len(a)):
            if not visited[i]:
                pro+=1
                dfs(i)
        return pro