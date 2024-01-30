'''
https://www.acmicpc.net/problem/15486

문제 풀이 과정

'''
import sys


input = lambda: sys.stdin.readline().rstrip()
N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]

max_value = 0
dp = [0]*(N+2)
for cur_d in range(N, 0, -1):
    t, p = tasks[cur_d-1]

    n_d = cur_d + t
    if n_d <= N+1:
        if max_value < dp[n_d]+p:
            dp[cur_d] = dp[n_d]+p
            max_value = dp[cur_d]
        else:
            dp[cur_d] = max_value
    else:
        dp[cur_d] = max_value
print(max_value)
