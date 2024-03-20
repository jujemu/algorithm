import sys
sys.setrecursionlimit(100_000)


def has_cycle(x, y):
    return x == y


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(x, y, w):
    global answer, last_weight

    x = find_parent(x)
    y = find_parent(y)

    if not has_cycle(x, y):
        parents[x] = y
        answer += w
        last_weight = w


input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

roads.sort(key=lambda x: x[2])

answer, last_weight = 0, None
parents = [i for i in range(N+1)]
for a, b, weight in roads:
    union(a, b, weight)

print(answer - last_weight)
