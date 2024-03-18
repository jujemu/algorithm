import sys


input = lambda: sys.stdin.readline()
N = int(input())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ROOT = 1
s = [(ROOT, None)]

answer = [0]*(N+1)
while s:
    curr, parent = s.pop()
    for adj in g[curr]:
        if adj != parent:
            answer[adj] = curr
            s.append((adj, curr))
print(*answer[2:], sep="\n")
