N, M = map(int, input().split())
blocks = [
    list(map(int, input().split())) for _ in range(N)
]

answer = 0

visited = [
    [False] * M for _ in range(N)
]
di = [
    [[0, -1], [0, 0], [1, 0]],
    [[0, -1], [0, 0], [-1, 0]],
    [[-1, 0], [0, 0], [0, 1]],
    [[1, 0], [0, 0], [0, 1]]
]


def check(x, y, i):
    for j in range(3):
        nx, ny = x + di[i][j][0], y + di[i][j][1]
        visited[nx][ny] = True


def uncheck(x, y, i):
    for j in range(3):
        nx, ny = x + di[i][j][0], y + di[i][j][1]
        visited[nx][ny] = False


def bt(x, y, result):
    global answer
    answer = max(answer, result)
    if x < 0 or N <= x or y < 0 or M <= y:
        return

    for i in range(4):
        tmp = 0
        available = True
        for j in range(3):
            nx, ny = x+di[i][j][0], y+di[i][j][1]
            if nx < 0 or N <= nx or ny < 0 or M <= ny or visited[nx][ny]:
                available = False
                break
            tmp += blocks[nx][ny] if j != 1 else blocks[nx][ny] * 2

        if y == M - 1:
            nx, ny = x + 1, 0
        else:
            nx, ny = x, y + 1

        if available:
            check(x, y, i)
            bt(nx, ny, result + tmp)
            uncheck(x, y, i)

    bt(nx, ny, result)


bt(0, 0, 0)
print(answer)
