import sys
sys.stdin = open('./dp/input_04.txt')

# input
N = int(input())

# dp list
dp = [0] * N
dp[0] = 1
dp[1] = 3
for n in range(2, N):
    dp[n] = dp[n-2] * 3 + dp[n-1]

# output
print(dp[-1] % 796796)
