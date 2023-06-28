from collections import deque
from itertools import combinations
import sys
import time
sys.stdin = open('./implementation/input_bj_14502.txt')
input = sys.stdin.readline
cur = time.time()

# input
N, M = map(int, input().split())
virus = []
empty = []
g = []
for x in range(N):
    tmp = list(map(int, input().split()))
    g.append(tmp)
    for y in range(M):
        if tmp[y] == 2:
            virus.append((x, y))
        elif tmp[y] == 0:
            empty.append((x, y))

# bfs
# R, D, L, U
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
check = [[False] * M for _ in range(N)]
def bfs():
    q = deque()
    for v in virus:
        check[v[0]][v[1]] = True
        q.append(v)
        
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and not g[nx][ny] and not check[nx][ny]:
                check[nx][ny] = True
                q.append((nx, ny))

def get_area():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] or check[i][j]:
                continue
            cnt += 1
    return cnt

# combination of empty
empty = combinations(empty, 3)

# get max of available area
result = 0
for emp in empty:
    for x, y in emp:
        g[x][y] = 1
    bfs()
    result = max(get_area(), result)
    check = [[False] * M for _ in range(N)]
    for x, y in emp:
        g[x][y] = 0
print(result)
print(time.time() - cur)
