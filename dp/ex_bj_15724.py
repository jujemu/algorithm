from collections import deque
import heapq
import math
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
g = [[]] + [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]
acc = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if i == 1:
            acc[i][j] = acc[i][j-1] + g[i][j]
        acc[i][j] = acc[i-1][j] + acc[i][j-1] + g[i][j] - acc[i-1][j-1]

K = int(input().rstrip())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    result = 0

    result += acc[x2][y2]
    result -= acc[x1-1][y2]
    result -= acc[x2][y1-1]
    result += acc[x1-1][y1-1]
    print(result)