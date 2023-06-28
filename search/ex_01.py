import sys
import time
sys.stdin = open('input_01.txt')
current = time.time()

# U, D, R, L
dx = (0, 0, 1, -1)
dy = (-1, 1, 0, 0)
def dfs(graph, vertex, visited, N, M):
    x, y = vertex
    if x < 0 or x >= M or y < 0 or y >= N or visited[y][x] or graph[y][x] == 1:
        return False
    visited[y][x] = True
    
    for dx_, dy_ in zip(dx, dy):
        dfs(graph, (x+dx_, y+dy_), visited, N, M)
    return True


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if not graph[i][j] and not visited[i][j]:
            if dfs(graph, (j, i), visited, N, M):
                cnt += 1
# print(graph)
# print(visited)
print(cnt)
print(time.time() - current)
