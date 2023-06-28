import sys
sys.stdin = open('./dp/input_03.txt')

# input
N = int(input())
K_list = list(map(int, input().split()))

# dp list
dp = [0] * N
dp[0], dp[1] = K_list[0], K_list[1]
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + K_list[i])

# output
print(dp[-1])
