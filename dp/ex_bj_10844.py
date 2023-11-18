import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stair = [[0] + [1 for _ in range(1, 10)]] + [[0 for _ in range(10)] for _ in range(N-1)]

for i in range(1, N):
    for j in range(10):
        if j-1 >= 0:
            stair[i][j] += stair[i-1][j-1]
        if j+1 < 10:
            stair[i][j] += stair[i-1][j+1]
print(sum(stair[-1]) % 1000000000)