class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = set()
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for n in adj[node]:
                if n != prev:
                    if not dfs(n, node):  
                        return False
            return True

        return dfs(0, -1) and len(visited) == n
