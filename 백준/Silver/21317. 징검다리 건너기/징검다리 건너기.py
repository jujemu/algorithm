import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
jumps = [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())

result = None

# 매우 큰 점프를 하지 않는 경우
dp = [0] * N
if N > 1:
    dp[0], dp[1] = 0, jumps[0][0]

for idx in range(2, N):
    dp[idx] = min(dp[idx-1] + jumps[idx-1][0], dp[idx-2] + jumps[idx-2][1])
result = dp[-1]

# 매우 큰 점프를 각 구간마다 적용하고 dp 적용
dp = [0] * N
if N > 1:
    dp[0], dp[1] = 0, jumps[0][0]

for k_idx in range(N-3):
    for idx in range(2, N):
        if idx == k_idx+3:
            dp[idx] = K + dp[idx-3]
            continue

        dp[idx] = min(dp[idx-1] + jumps[idx-1][0], dp[idx-2] + jumps[idx-2][1])
    result = min(dp[-1], result)
print(result)
