import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
sche = [list(map(int, input().split())) for _ in range(N)]

max_value = 0
dp = [0] * (N+1)
for idx in range(N-1, -1, -1):
    t, p = sche[idx]
    if idx + t <= N:
        max_value = max(max_value, dp[idx+t] + p)
    dp[idx] = max_value
print(max_value)