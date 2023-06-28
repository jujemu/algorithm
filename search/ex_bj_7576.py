from collections import deque
import sys
sys.stdin = open('./search/input_bj_7576.txt')
input = sys.stdin.readline

# input
# number of cols, rows
M, N = map(int, input().split())
g = [list(map(int, input().rstrip().split())) for _ in range(N)]

ripped = []
for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            ripped.append((i, j))

def check():
    for i in range(N):
        for j in range(M):
            if not g[i][j]:
                return False
    return True

# R, D, L, U
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs():
    cnt = 0
    
    q = deque()
    for x, y in ripped:
        g[x][y] = -1
        q.append((x, y, cnt))
        
    while q:
        x, y, cnt = q.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<= nx < N and 0<= ny < M and not g[nx][ny]:
                q.append((nx, ny, cnt+1))
                g[nx][ny] = -1
    return cnt
        
result = bfs()
print(result if check() else -1)
