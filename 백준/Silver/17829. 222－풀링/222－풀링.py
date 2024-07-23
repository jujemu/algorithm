import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
matrix = [
    list(map(int, input().split()))
    for _ in range(N)
]

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def rec(arr):
    if len(arr) == 1:
        return arr[0][0]

    n = len(arr)
    next_arr = [
        [None] * (n//2)
        for _ in range(n//2)
    ]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            tmp = []
            for k in range(4):
                ni, nj = i+dx[k], j+dy[k]
                tmp.append(arr[ni][nj])
            tmp.sort()
            next_arr[i//2][j//2] = tmp[-2]

    return rec(next_arr)


print(rec(matrix))
