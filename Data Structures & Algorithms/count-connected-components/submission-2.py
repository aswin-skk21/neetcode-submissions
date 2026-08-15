class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = defaultdict(list)

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(node):
            visit.add(node)
            for n in adj[node]:
                if n not in visit:
                    dfs(n)
        
        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        
        return count