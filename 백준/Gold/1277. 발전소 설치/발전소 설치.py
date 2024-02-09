"""
https://www.acmicpc.net/problem/1277

발전소 -> 노드
전선 -> 간선

제한 조건
 - 간선의 길이의 최대값

구현
 - 다익스트라
 - 각 발전소에서 모든 발전소로 연결되어 있다고 가정
 - 주어진 전선은 비용이 0

다익스트라
출발 노드로부터 각 노드까지의 거리 테이블
핵심이 되는게 현재 방문하지 않은 노드 중에 최소 거리를 뽑아야한다.
처음에 초기화를 어떻게 하지? -> INF
지금 고민하는 문제 -> 모든 노드를 연결해서 간선 정보를 heap에 넣으면 이거 장난아냐, 되는지 안되는지 판단이 안선다.
"""
import heapq
from math import sqrt
import sys


def get_wire_length_(x1, y1, x2, y2):
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)


def get_wire_length(a, b):
    if b in adj[a]:
        return 0

    (x1, y1), (x2, y2) = plants[a], plants[b]
    return get_wire_length_(x1, y1, x2, y2)


input = lambda: sys.stdin.readline().rstrip()
N, W = map(int, input().split())
M = float(input())
plants = {i: tuple(map(int, input().split())) for i in range(1, N+1)}

adj = [[] for _ in range(N+1)]
for _ in range(W):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

INF = int(1e11)
dist_table = [INF] * (N+1)
dist_table[1] = 0

heap = [(0, 1)]
visited = [False] * (N+1)
while heap:
    if visited[N]:
        break

    dist, n = heapq.heappop(heap)
    if visited[n]:
        continue

    visited[n] = True
    dist_table[n] = dist
    for next in range(1, N+1):
        if visited[next]:
            continue

        next_dist = get_wire_length(n, next)
        if next_dist <= M:
            heapq.heappush(heap, (dist + next_dist, next))

print(int(dist_table[N]*1000))
