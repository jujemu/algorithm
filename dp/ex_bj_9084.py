import sys
input = lambda: sys.stdin.readline().rstrip()

result = []
for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target+1)
    dp[0] = 1
    for coin in coins:
        for idx in range(coin, target+1):
            dp[idx] += dp[idx-coin]
    # result.append(dp[-1])
    result.append(dp[-1])
print(*result, sep="\n")