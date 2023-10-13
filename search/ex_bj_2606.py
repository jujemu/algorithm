import sys
input = sys.stdin.readline

# DFS
# 인접 리스트
N = int(input())
K = int(input())
visited = [False] * (N+1)
arr = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(arr, start):
    visited[start] = True
    for adj in arr[start]:
        if visited[adj]:
            continue

        dfs(arr, adj)

dfs(arr, 1)
print(sum(visited) - 1)
