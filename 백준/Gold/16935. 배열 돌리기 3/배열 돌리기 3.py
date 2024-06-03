N, M, R = map(int, input().split())
A = [
    [*map(int, input().split())]
    for _ in range(N)
]
Rs = [*map(int, input().split())]


# N, M, R = 4, 4, 1
# A = [
#     [1, 2, 3, 4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# Rs = [1]


def op1():
    global A
    A = A[::-1]


def op2():
    global A
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = A[i][M-j-1]
    A = tmp


def op3():
    global A, N, M

    tmp = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            tmp[i][j] = A[N-j-1][i]
    A = tmp
    N, M = M, N


def op4():
    global A, N, M

    tmp = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            tmp[i][j] = A[j][M-i-1]
    A = tmp
    N, M = M, N


def op5():
    global A

    tmp = [[0]*M for _ in range(N)]
    NN, MM = N//2, M//2
    for i in range(NN):
        for j in range(MM):
            tmp[i][j] = A[i+NN][j]
    for i in range(NN):
        for j in range(MM, M):
            tmp[i][j] = A[i][j-MM]
    for i in range(NN, N):
        for j in range(MM, M):
            tmp[i][j] = A[i-NN][j]
    for i in range(NN, N):
        for j in range(MM):
            tmp[i][j] = A[i][j-MM]
    A = tmp


def op6():
    global A

    tmp = [[0] * M for _ in range(N)]
    NN, MM = N // 2, M // 2
    for i in range(NN):
        for j in range(MM):
            tmp[i][j] = A[i][j+MM]
    for i in range(NN):
        for j in range(MM, M):
            tmp[i][j] = A[i+NN][j]
    for i in range(NN, N):
        for j in range(MM, M):
            tmp[i][j] = A[i][j-MM]
    for i in range(NN, N):
        for j in range(MM):
            tmp[i][j] = A[i-NN][j]
    A = tmp


for r in Rs:
    if r == 1:
        op1()
    elif r == 2:
        op2()
    elif r == 3:
        op3()
    elif r == 4:
        op4()
    elif r == 5:
        op5()
    elif r == 6:
        op6()

for i in range(N):
    for j in range(M):
        print(A[i][j], end=" ")
    print()
