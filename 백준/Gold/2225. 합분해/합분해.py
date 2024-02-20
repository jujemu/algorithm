"""
https://www.acmicpc.net/problem/2225
"""
N, K = map(int, input().split())

dp = [[1] * (N+1)] + [[0] * (N+1)]
for _ in range(K-1):
    for i in range(N+1):
        for j in range(N+1):
            if j-i >= 0:
                dp[1][j] += dp[0][j-i]
    dp[0] = dp[1]
    dp[1] = [0] * (N+1)
print(dp[0][-1] % 1000000000)
