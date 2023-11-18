import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n >= 2:
    dp[1], dp[2] = 1, 3
for idx in range(3, n+1):
    dp[idx] = dp[idx-2] * 2 + dp[idx-1]
print(dp[-1] % 10007)