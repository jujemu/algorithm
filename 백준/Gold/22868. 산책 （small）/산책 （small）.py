from collections import deque
import sys


def go():
    q = deque([(S, 0, [])])
    visited = [False] * (N+1)

    result = None
    while q:
        curr, cost, p = q.popleft()
        if result and cost > result:
            return result

        if curr == E:
            result = cost
            path.append(p)
            continue

        if visited[curr]:
            continue

        visited[curr] = True
        for adj in graph[curr]:
            if not visited[adj]:
                q.append((adj, cost+1, p+[adj]))

    return result


def back():
    q = deque([(E, 0)])
    visited = [False] * (N+1)

    while q:
        curr, cost = q.popleft()
        if curr == S:
            return cost

        if visited[curr]:
            continue

        visited[curr] = True
        for adj in graph[curr]:
            if not visited[adj] and not passed[adj]:
                q.append((adj, cost+1))


def passed_route():
    path.sort()
    for n in path[0]:
        passed[int(n)] = True


input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if a != b:
        graph[a].append(b)
        graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
S, E = map(int, input().split())

answer = 0
path = []
answer += go()
passed = [False] * (N+1)
passed_route()

answer += back()

print(answer)
