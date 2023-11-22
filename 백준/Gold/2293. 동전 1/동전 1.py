import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = {int(input()) for _ in range(n)}
coins = [coin for coin in coins if coin <= k]

dp = [0] * (k+1)
for coin in coins:
    dp[coin] += 1
    for idx in range(1, k+1-coin):
        if dp[idx]:
            dp[idx+coin] += dp[idx]
print(dp[k])
