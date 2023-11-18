import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]
test = [list(map(int, input().split())) for _ in range(M)]

sum_grid = [[0] * (N+1) for _ in range(N+1)]
sum_grid[1][1] = grid[1][1]
for c in range(2, N+1):
    sum_grid[1][c] = sum_grid[1][c-1] + grid[1][c]
for r in range(2, N+1):
    sum_grid[r][1] = sum_grid[r-1][1] + grid[r][1]
for r in range(2, N+1):
    for c in range(2, N+1):
        sum_grid[r][c] = sum_grid[r][c-1] + sum_grid[r-1][c] - sum_grid[r-1][c-1] + grid[r][c]

for t in test:
    x1, y1, x2, y2 = t
    print(sum_grid[x2][y2] - sum_grid[x1-1][y2] - sum_grid[x2][y1-1] + sum_grid[x1-1][y1-1])
