from collections import deque
import sys
sys.stdin = open('./search/input_bj_7569.txt')
input = sys.stdin.readline

# input
M, N, H = map(int, input().split())
ripped = []
g = [[[0] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        tmp = list(map(int, input().split()))
        g[i][j] = tmp
        for k in range(M):
            if tmp[k] == 1:
                ripped.append([i, j, k])
            

# bfs
# R, D, L, U, up, down
d = [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
def bfs():
    cnt = 0
    q = deque()
    for rip in ripped:
        q.append(rip + [cnt])
    
    while q:
        x, y, z, cnt = q.popleft()
        for dx, dy, dz in d:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and not g[nx][ny][nz]:
                g[nx][ny][nz] = 1
                q.append([nx, ny, nz, cnt+1])
    return cnt

def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not g[i][j][k]:
                    return False
    return True

# output
result = bfs()
print(result if check() else -1)
