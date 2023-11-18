import sys
input = lambda: sys.stdin.readline().rstrip()

numbers = [int(input()) for _ in range(int(input()))]

dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4
for number in range(4, 11):
    for i in range(1, 4):
        dp[number] += dp[number-i]

for number in numbers:
    print(dp[number])