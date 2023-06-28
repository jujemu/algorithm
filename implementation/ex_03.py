import time
import sys
sys.stdin = open('../input_03.txt')

N, M = map(int, input().split())
x, y, direction = map(int, input().split())
visited = [[0]*M for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]

# forward step can be
# N, E, S, W
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

# initial state
cnt = 1
rotate_cnt = 0
visited[y][x] = 1

while True:
    direction -= 1
    if direction == -1:
        direction = 3

    tmp_x = x + dx[direction]
    tmp_y = y + dy[direction]
    if visited[tmp_y][tmp_x] + arr[tmp_y][tmp_x] >= 1:
        rotate_cnt += 1
        if rotate_cnt >= 4:
            rotate_cnt = 0
            tmp_x = x - dx[direction]
            tmp_y = y - dy[direction]
            if arr[tmp_y][tmp_x] == 1:
                break
            else:
                x -= dx[direction]
                y -= dy[direction]
                continue
        continue

    rotate_cnt = 0
    x, y = tmp_x, tmp_y
    visited[y][x] = 1
    cnt += 1
    # print(y, x)
print(cnt)
