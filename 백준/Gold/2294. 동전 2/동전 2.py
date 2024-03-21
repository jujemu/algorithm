import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    dp = [0]*(k+1)
    coin = set()
    queue = deque()
    for _ in range(n):
        c = int(input())
        if c <= k:
            coin.add(c)
            queue.append((c, 2))
            dp[c] = 1
    coin = sorted(coin)
    while queue:
        i, cnt = queue.popleft()
        if i == k:
            break
        for c in coin:
            if i+c > k:
                break
            if dp[i+c] == 0:
                dp[i+c] = cnt
                queue.append((i+c, cnt+1))
    print(dp[k] if dp[k] else -1)

solution()