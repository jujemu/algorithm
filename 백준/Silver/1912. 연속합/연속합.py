import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
numbers = list(map(int, input().split()))

dp = [0] * n
dp[0] = numbers[0]
for idx in range(1, n):
    if numbers[idx] < 0 and dp[idx-1] + numbers[idx] < 0:
        dp[idx] = 0
        continue
    dp[idx] = dp[idx-1] + numbers[idx]

for idx in range(n):
    if numbers[idx] > 0:
        break
    if idx == n-1:
        if numbers[idx] < 0:
            value = max(numbers)
            dp = [value, value-1]
print(max(dp))
