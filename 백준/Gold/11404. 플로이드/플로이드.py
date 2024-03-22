import sys


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = int(input())

INF = int(1e9)
matrix = [[]]
for i in range(n):
    tmp = [0]
    for j in range(n):
        if i == j:
            tmp.append(0)
        else:
            tmp.append(INF)
    matrix.append(tmp)

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a][b] = min(c, matrix[a][b])

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == INF:
            print(0, end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
