import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
for _ in range(int(input())):
    n, d = map(int, input().split())
    d = d // 45 % 8
    n_2 = n//2

    grid = [list(map(int, input().split())) for _ in range(n)]
    moved_grid = [[0] * n for _ in range(n)]

    for _ in range(d):
        for r in range(n):
            for c in range(n):
                # 주 대각선
                if r == c:
                    moved_grid[r][n_2] = grid[r][c]
                    continue
                # 가운데 열
                if c == n_2:
                    moved_grid[r][n-r-1] = grid[r][c]
                    continue
                # 부 대각선
                if r + c == n-1:
                    moved_grid[n_2][c] = grid[r][c]
                # 가운데 행
                if r == n_2:
                    moved_grid[c][c] = grid[r][c]
        for r in range(n):
            for c in range(n):
                if not moved_grid[r][c]:
                    moved_grid[r][c] = grid[r][c]
        grid = moved_grid
        moved_grid = [[0] * n for _ in range(n)]
    result.append(grid)

for res in result:
    for row in res:
        print(*row, sep=" ")