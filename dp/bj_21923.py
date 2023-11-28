import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)][::-1]

dp_up = [[0] * M for _ in range(N)]
dp_down = [[0] * M for _ in range(N)]
dp_up[0][0] = grid[0][0]
dp_down[0][-1] = grid[0][-1]

for i in range(1, N):
    dp_up[i][0] = grid[i][0] + dp_up[i-1][0]
    dp_down[i][-1] = grid[i][-1] + dp_down[i-1][-1]
for j in range(1, M):
    dp_up[0][j] = grid[0][j] + dp_up[0][j-1]
    dp_down[0][-j-1] = grid[0][-j-1] + dp_down[0][-j]

for i in range(1, N):
    for j in range(1, M):
        dp_up[i][j] = max(dp_up[i-1][j], dp_up[i][j-1]) + grid[i][j]

for i in range(1, N):
    for j in range(M-2, -1, -1):
        dp_down[i][j] = max(dp_down[i-1][j], dp_down[i][j+1]) + grid[i][j]

max_value = -int(1e9)
for i in range(N):
    for j in range(M):
        max_value = max(max_value, dp_up[i][j] + dp_down[i][j])
print(max_value)