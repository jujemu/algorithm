from collections import deque
import sys
sys.stdin = open('./search/input_bj_2178.txt')
input = sys.stdin.readline

# input
N, M = map(int, input().split())
g = [list(map(int, input().rstrip())) for _ in range(N)]
check = [[False] * M for _ in range(N)]

# R, D, L, U
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs():
    cnt = 1
    check[0][0] = True
    q = deque([(0, 0, cnt)])
        
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (N-1, M-1):
            return cnt
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or not g[nx][ny] or check[nx][ny]:
                continue
            
            check[nx][ny] = True
            q.append((nx, ny, cnt+1))

print(bfs())
