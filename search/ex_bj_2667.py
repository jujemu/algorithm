from collections import deque
import sys
input = sys.stdin.readline
# sys.stdin = open('input_bj_2667.txt')


# U, D, L, R
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
def bfs(x, y):
    cnt = 0
    q = deque([(x, y)])
    graph[y][x] = 0
    
    while q:
        # print(q)
        cnt += 1
        x, y = q.popleft()
        for dx_, dy_ in zip(dx, dy):
            tmp_x = x + dx_
            tmp_y = y + dy_
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or not graph[tmp_y][tmp_x]:
                continue
            q.append((tmp_x, tmp_y))
            graph[tmp_y][tmp_x] = 0
    # print()
    return cnt

# input
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
block_cnt = 0
arr_cnt = []

# traverse
for i in range(N):
    for j in range(N):
        if not graph[i][j]:
            continue
        # print(*graph, sep='\n')
        # print()
        arr_cnt.append(bfs(j, i))
        block_cnt += 1
arr_cnt.sort()

# output
print(block_cnt)
print(*arr_cnt, sep='\n')
