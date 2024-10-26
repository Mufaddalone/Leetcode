class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n+1)]
        size = [0] *(n+1)
        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(u,v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return 
            if size[root_u] > size[root_v]:
                size[root_u] += size[root_v]
                parent[root_v] = root_u
            else:
                size[root_v] += size[root_u]
                parent[root_u] = root_v
        z = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in z:
                    z[mail] = i
                else:
                    union(i, z[mail])
        
        # Collect emails by root parent index
        mergemail = defaultdict(list)
        for mail, node in z.items():
            root_node = find(node)
            mergemail[root_node].append(mail)

        # Build the final output
        ans = []
        for idx, emails in mergemail.items():
            name = accounts[idx][0]
            emails.sort()
            ans.append([name] + emails)
        
        return ans