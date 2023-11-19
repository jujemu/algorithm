import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

def solve():
    dp = [0] * (n+1)
    dp[1] = 1

    if n <= 1:
        return dp[-1]
    
    dp[2] = 2
    for idx in range(3, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]
    return dp[-1]

print(solve() % 10007)

