import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    if n <= 2:
        if n == 1:
            print(max(dp[0][0], dp[1][0]))
        if n == 2:
            print(max(dp[0][0] + dp[1][1], dp[0][1] + dp[1][0]))
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for idx in range(2, n):
            dp[0][idx] += max(dp[1][idx-1], dp[1][idx-2])
            dp[1][idx] += max(dp[0][idx-1], dp[0][idx-2])
        arr.append(max(dp[0][n-1], dp[1][n-1]))
print(*arr, sep="\n")