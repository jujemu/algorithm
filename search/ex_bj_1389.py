from collections import deque
import sys
sys.stdin = open('./search/input_bj_1389.txt')
input = sys.stdin.readline

# input
N, M = map(int, input().split())
g = [set() for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    g[x].add(y)
    g[y].add(x)

# bfs
def bfs(start):
    q = deque()
    cnt = 0
    visited = [False] * (N+1)
    result = 0
    
    # initial
    q.append([start, cnt])
    visited[start] = True
    
    while q:
        current, cnt = q.popleft()
        for adj in g[current]:
            if not visited[adj]:
                result += cnt+1
                visited[adj] = True
                q.append((adj, cnt+1))
    return result

# traverse
answer = [123456789] * (N+1)
for i in range(1, N+1):
    answer[i] = bfs(i)

# output
idx, mn = 0, 123456789
for i, ele in enumerate(answer[1:], start=1):
    if mn > ele:
        idx = i
        mn = ele
print(idx)
