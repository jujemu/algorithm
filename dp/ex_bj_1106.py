import sys
input = lambda: sys.stdin.readline().rstrip()

C, N = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
max_reword = max(cities, key=lambda x: x[1])[1]

INF = int(1e9)
dp = [INF] * (C+1+max_reword)
dp[0] = 0

# max_reword가 필요한 이유는?
# max_reword가 없었다면, C가 모든 reword보다 작을 때는?
# cities를 정렬해야할까?
for cost, reword in cities:
    for cur in range(reword, C+1+max_reword):
        dp[cur] = min(dp[cur-reword] + cost, dp[cur])
# print(dp)
print(min(dp[C:]))