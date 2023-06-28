import sys
import time
sys.setrecursionlimit(250000)
sys.stdin = open('./search/input_bj_1520.txt')
input = sys.stdin.readline
current = time.time()

# input
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
tracked_g = [[0] * N for _ in range(M)]
tracked_g[M-1][N-1] = 1

# dfs
# R, D, L, U
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(x, y):
    if (x, y) == (M-1, N-1):
            return True
    tmp = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy        
        if nx < 0 or nx >= M or ny < 0 or ny >= N or graph[nx][ny] >= graph[x][y]:
            continue  
        
        # 1
        if tracked_g[nx][ny] == -1:
            continue
        
        if not tracked_g[nx][ny]:
            if dfs(nx, ny):            
                tmp += tracked_g[nx][ny]
        else:
            tmp += tracked_g[nx][ny]            
                
    if not tmp:
        tracked_g[x][y] = -1
        return False
    else:
        tracked_g[x][y] = tmp
        return True
    
# count available path
dfs(0, 0)

# output
# print(*tracked_g, sep='\n')
print(tracked_g[0][0] if tracked_g[0][0] != -1 else 0)
print('processing time is :', time.time() - current)
