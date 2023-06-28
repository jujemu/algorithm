import sys
sys.setrecursionlimit(1001)
sys.stdin = open('input_bj_11724.txt')
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    
    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)
    

# input
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
graph = [sorted(adj) for adj in graph]
visited = [False] * (N+1)

# traverse
cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
    