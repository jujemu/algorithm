import heapq
import sys
PATH = "input/"
PROBLEM_NUM = "bj18352"

input = sys.stdin.readline

INF = int(1e9)
N, M, K, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
acc_list = [INF] * (N + 1)
visited = [False] * (N + 1)

# fill out the graph
for _ in range(M):
    n, e = map(int, input().split())
    graph[n].append(e)

def dijkstra(start):
    acc_list[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        acc, cur = heapq.heappop(q)

        # 방문한 노드일 경우, 넘어가기
        if visited[cur]:
            continue
        
        visited[cur] = True
        for next in graph[cur]:
            if acc + 1 < acc_list[next]:
                acc_list[next] = acc + 1
            heapq.heappush(q, (acc_list[next], next))

dijkstra(start)

result = sorted([idx for idx, acc in enumerate(acc_list) if acc == K])

if result:
    print(*result, sep='\n')
else:
    print(-1)
