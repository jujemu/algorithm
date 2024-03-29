import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
max_value = 0

for idx in range(N-1, -1, -1):
    t, p = schedule[idx]
    if idx + t > N:
        dp[idx] = max_value
    else:
        dp[idx] = max(max_value, p + dp[idx+t])
        max_value = dp[idx]
print(dp[0])