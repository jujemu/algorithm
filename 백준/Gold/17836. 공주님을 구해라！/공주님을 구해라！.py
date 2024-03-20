from collections import deque
import sys


input = lambda: sys.stdin.readline().rstrip()
N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = "Fail"
visited = [[False]*M for _ in range(N)]
visited_with_gram = [[False]*M for _ in range(N)]
q = deque([(0, 0, 0, False)])
while q:
    x, y, t, with_gram = q.popleft()

    # 시간이 초과한 경우
    if t > T:
        answer = "Fail"
        break

    # 공주를 구함
    if (x, y) == (N-1, M-1):
        answer = t
        break

    # 이미 방문한 경우
    if with_gram:
        if visited_with_gram[x][y]:
            continue
    elif visited[x][y]:
        continue

    # 그람을 획득
    if graph[x][y] == 2:
        with_gram = True

    visited[x][y] = True
    if with_gram:
        visited_with_gram[x][y] = True

    for d in range(4):
        nx, ny = x + dx[d], y+dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if with_gram and not visited_with_gram[nx][ny]:
                q.append((nx, ny, t+1, with_gram))

            elif not visited[nx][ny] and graph[nx][ny] != 1:
                q.append((nx, ny, t+1, with_gram))

print(answer)
