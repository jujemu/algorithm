from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y):
    cnt = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        if visited[x][y]:
            continue

        visited[x][y] = True
        cnt += 1
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and g[nx][ny]:
                q.append((nx, ny))

    return cnt


N = int(input())
g = [list(map(int, input())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and g[i][j]:
            answer.append(bfs(i, j))

answer = [len(answer)] + sorted(answer)
print(*answer, sep="\n")