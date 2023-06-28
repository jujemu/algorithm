import sys
sys.stdin = open('./search/input_bj_1967.txt')
input = sys.stdin.readline

# input
N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c, w = map(int, input().split())
    g[p].append((c, w))
    g[c].append((p, w))

# find leave
leave = set()
for idx, vertex in enumerate(g):
    if len(vertex) == 1:
        leave.add(idx)

# dfs
def dfs(vertex, acc, start):
    if vertex in leave and vertex != start:
        global result
        result = max(result, acc)
        return
    
    for adj, w in g[vertex]:
        if not visited[adj]:
            visited[adj] = True
            dfs(adj, acc+w, start)
    
# find the max length of tree in leave loop
result = 0
for leaf in leave:
    visited = [False] * (N+1)
    visited[leaf] = True
    dfs(leaf, 0, leaf)

# output
print(result)
