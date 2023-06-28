import sys
sys.stdin = open('./dp/input_05.txt')
input = sys.stdin.readline

# input
N, M = map(int, input().split())
coins = set()
for _ in range(N):
    coin = int(input().rstrip())
    if coin <= M:
        coins.add(coin)

# dp list
dp = [0] * (M+1)
for coin in coins:
    dp[coin] += 1

# bottom-up
for i in range(1, M+1):
    tmp = 10001
    for coin in coins:
        if dp[i]:
            continue
        if i-coin > 0 and dp[i-coin]:
            tmp = min(dp[i-coin], tmp)
    dp[i] = tmp + 1 if tmp != 10001 else dp[i]
print(*dp, sep=' ')
print(dp[M] if dp[M] else -1)
    