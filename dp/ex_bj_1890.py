import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visit_acc = [[0] * N for _ in range(N)]
visit_acc[0][0] = 1

for r in range(N):
    for c in range(N):
        current_jump = grid[r][c]
        if visit_acc[r][c] == 0 or current_jump == 0:
            continue
                
        nr = r + current_jump
        nc = c + current_jump

        if nc < N:
            visit_acc[r][nc] += visit_acc[r][c]
        if nr < N:
            visit_acc[nr][c] += visit_acc[r][c]
        print(r, c)
        print(*visit_acc, sep="\n")
        print()
print(visit_acc[N-1][N-1])