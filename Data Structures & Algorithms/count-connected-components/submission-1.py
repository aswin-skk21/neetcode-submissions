class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = defaultdict(list)

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)

        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1

        return count