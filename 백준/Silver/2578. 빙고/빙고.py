def find_x(x, bingo):
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == x:
                bingo[r][c] = 0
                return r, c


def 상우대각선():
    for z in range(5):
        if bingo[z][4 - z] != 0:
            return 0
    return 1


def 상하대각선():
    for z in range(5):
        if bingo[z][z] != 0:
            return 0
    return 1


def 행(r):
    for z in range(5):
        if bingo[r][z] != 0:
            return 0
    return 1


def 열(c):
    for z in range(5):
        if bingo[z][c] != 0:
            return 0
    return 1


yo = 0
bingo = [[*map(int, input().split())] for _ in range(5)]
for i in range(5):
    for j, x in enumerate(map(int, input().split()), start=1):
        r, c = find_x(x, bingo)

        if r+c == 4:
            yo += 상우대각선()
        if r == c:
            yo += 상하대각선()

        yo += 행(r)
        yo += 열(c)
        if yo >= 3:
            print(i*5 + j)
            exit()