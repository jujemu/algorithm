import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * N
dp[0] = True

for idx in range(N):
        for next in range(idx+1, N):
            if dp[idx] and (next-idx) * (1+abs(A[next]-A[idx])) <= K:
                dp[next] = True
print("YES" if dp[-1] else "NO")