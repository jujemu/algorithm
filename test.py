import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6+1)

N = int(input())
adj_matrix = [[] for _ in range(N+1)]
for i in range(N-1):
    node_1, node_2 = list(map(int, input().split()))
    adj_matrix[node_1].append(node_2)
    adj_matrix[node_2].append(node_1)

parent = [None] * (N+1)
visited = [False] * (N+1)
def dfs(cur_parent):
    visited[cur_parent] = True
    for adj in adj_matrix[cur_parent]:
        if not visited[adj]:
            parent[adj] = cur_parent
            dfs(adj)
dfs(1)
print(*parent[2:], sep="\n")