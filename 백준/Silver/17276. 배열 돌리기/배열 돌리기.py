def get_parts():
    parts = []
    parts.append([grid[i][n // 2] for i in range(n)])
    parts.append([grid[i][i] for i in range(n)])
    parts.append([grid[n // 2][i] for i in range(n)])
    parts.append([grid[n - i - 1][i] for i in range(n)])
    return parts


T = int(input())
answer = []
for _ in range(T):
    n, d = map(int, input().split())
    d //= 45
    if d > 0:
        d = 8 - d
    else:
        d *= -1

    grid = [list(map(int, input().split())) for _ in range(n)]
    parts = get_parts()
    tmp = []
    for _ in range(d):
        tmp.append(parts[-1][::-1])
        tmp.extend(parts[:3])
        parts = tmp
        tmp = []

    for i, ele in enumerate(parts[0]):
        grid[i][n//2] = ele
    for i, ele in enumerate(parts[1]):
        grid[i][i] = ele
    for i, ele in enumerate(parts[2]):
        grid[n//2][i] = ele
    for i, ele in enumerate(parts[3]):
        grid[n-i-1][i] = ele
    answer.append(grid)

for i in range(T):
    for j in range(len(answer[i])):
        print(*answer[i][j], sep=" ")