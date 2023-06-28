import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input_bj_1012.txt')
input = sys.stdin.readline

# U, D, L, R
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def dfs(v):
    x, y = v
    graph[y][x] = 0
    
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N or not graph[ny][nx]:
            continue
        dfs((nx, ny))
    

for _ in range(int(input())):
    # input
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    # traverse
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                dfs((j, i))
                cnt += 1
    print(cnt)
    