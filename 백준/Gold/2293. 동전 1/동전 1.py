import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = [coin for coin in coins if coin <= 10000]

dp = [0] * (k+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[-1])