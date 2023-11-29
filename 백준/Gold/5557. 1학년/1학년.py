import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * (N-1) for _ in range(21)]
dp[numbers[0]][0] = 1

for c in range(1, N-1):
    for r in range(21):
        if r+numbers[c] < 21:
            dp[r+numbers[c]][c] += dp[r][c-1]
        if 0 <= r-numbers[c]:
            dp[r-numbers[c]][c] += dp[r][c-1]

print(dp[numbers[-1]][-1])