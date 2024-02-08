"""
https://www.acmicpc.net/problem/1976

"""
N, M = map(int, [input() for _ in range(2)])
parent = [i for i in range(N)]
adj = [list(map(int, input().split())) for _ in range(N)]


def find_parent(curr):
    p = parent[curr]
    if curr != p:
        parent[curr] = find_parent(p)
    return parent[curr]


def union(x, y):
    x, y = find_parent(x), find_parent(y)
    parent[x] = y
    return


for i in range(N):
    for j in range(i+1, N):
        if adj[i][j] == 1:
            union(i, j)

plan = [*map(lambda x: int(x)-1, input().split())]
result = True
pre_p = find_parent(plan[0])
for city in plan[1:]:
    if pre_p != find_parent(city):
        result = False
        break

print("YES" if result else "NO")
