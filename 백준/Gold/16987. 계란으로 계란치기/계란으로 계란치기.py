N = int(input())
eggs = [
    [*map(int, input().split())] for _ in range(N)
]

answer = 0


def hit(xi, yi):
    eggs[xi][0] -= eggs[yi][1]
    eggs[yi][0] -= eggs[xi][1]


def unhit(xi, yi):
    eggs[xi][0] += eggs[yi][1]
    eggs[yi][0] += eggs[xi][1]


def bt(i):
    global answer
    # print(i, eggs)

    if i == N or i == N-1 and eggs[i][0] <= 0:
        # print(eggs)
        cnt = sum([egg[0] <= 0 for egg in eggs])
        answer = max(answer, cnt)
        return

    if eggs[i][0] > 0:
        flag = False
        for j in range(N):
            if j == i or eggs[j][0] <= 0:
                continue

            flag = True
            hit(i, j)
            bt(i+1)
            unhit(i, j)
        if not flag:
            answer = max(answer, N-1)
            return
    else:
        bt(i + 1)


bt(0)
print(answer)
