import sys
sys.setrecursionlimit(1_000_000)

N = 1_000_001
edge_in = [0] * N
edge_out = [[] for _ in range(N)]
result = [0, 0, 0]
visited = [False] * N

def solution(edges):
    for a, b in edges:
        edge_in[b] += 1
        edge_out[a].append(b)
        
    additional_node = None
    for node in range(1, N):
        if is_additional_node(node):
            additional_node = node
            break
    
    for adj in edge_out[additional_node]:
        index = dfs(adj, visited)
        if not index:
            index = 0
            
        result[index] += 1
    
    return [additional_node] + result
    
    
def is_additional_node(n):
    return not edge_in[n] and len(edge_out[n]) >= 2


def dfs(cur, visited):
    if visited[cur]:
        return
    
    visited[cur] = True
    if len(edge_out[cur]) == 2:
        return 2
    
    if not edge_out[cur]:
        return 1
    
    for adj in edge_out[cur]:
        if not visited[adj]:
            return dfs(adj, visited)