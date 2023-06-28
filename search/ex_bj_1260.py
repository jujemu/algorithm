from collections import deque
import sys
sys.stdin = open('input_bj_1260.txt')


def dfs(graph, vertex, visited):
    if visited[vertex]:
        return
    print(vertex, end=' ')
    visited[vertex] = True
    
    for v in graph[vertex]:
        dfs(graph, v, visited)


def bfs(graph, vertex, visited):
    q = deque([vertex])
    visited[vertex] = True
    
    while q:
        vertex = q.popleft()
        print(vertex, end=' ')
        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


N, M, start = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for m in range(M):
    x, y = map(int, input().split())
    if y not in graph[x]:
        graph[x].append(y)
    if x not in graph[y]:
        graph[y].append(x)
graph = [sorted(element) for element in graph]

dfs(graph, start, visited)
print()

visited = [False] * (N+1)
bfs(graph, start, visited)
