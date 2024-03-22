from heapq import heappush, heappop
import sys


input = lambda: sys.stdin.readline().rstrip()
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

INF = int(1e9)
distance = [INF] * (V+1)
visited = [False] * (V+1)

heap = [(0, K)]
while heap:
    cost, curr = heappop(heap)
    if visited[curr]:
        continue

    distance[curr] = min(distance[curr], cost)
    visited[curr] = True
    for adj, w in graph[curr]:
        if not visited[adj]:
            heappush(heap, (cost+w, adj))

for d in distance[1:]:
    if d != INF:
        print(d)
    else:
        print("INF")
