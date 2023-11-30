import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

dp = [[0] * (T+1) for _ in range(k)]
dp[0][0] = 1

for i in range(k):
    c_coin, c_number = coins[i]
    for j in range(T, -1, -1):
        if i:
            dp[i][j] = dp[i-1][j]

        if dp[i][j]:
            for n in range(c_coin, min(T-j, c_coin*c_number)+1, c_coin):
                dp[i][j+n] += dp[i][j]
print(dp[-1][-1])

