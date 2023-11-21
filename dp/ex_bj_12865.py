import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
items = sorted([list(map(int, input().split())) for _ in range(N)], reverse=True)

dp = [[0]*(K+1) for _ in range(N)]
init_w, init_v = items[0]
for idx in range(init_w, K+1):
    dp[0][idx] = init_v

for r, item in enumerate(items[1:], start=1):
    w, v = item
    for c in range(w, K+1):
        dp[r][c] = max(dp[r-1][c-w]+v, dp[r-1][c])
print(dp[-1][K])