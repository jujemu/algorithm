import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = input(), input()
dp = [[0]*len(B) for _ in range(len(A))]

for b_idx in range(len(B)):
    if B[b_idx] == A[0]:
        for idx in range(b_idx, len(B)):
            dp[0][idx] = 1
        break

for a_idx in range(len(A)):
    if B[0] == A[a_idx]:
        for idx in range(a_idx, len(A)):
            dp[idx][0] = 1
        break

for a_idx in range(1, len(A)):
    for b_idx in range(1, len(B)):
        if A[a_idx] == B[b_idx]:
            dp[a_idx][b_idx] = dp[a_idx-1][b_idx-1]+1
        else:
            dp[a_idx][b_idx] = max(dp[a_idx][b_idx-1], dp[a_idx-1][b_idx])
# print(*dp, sep="\n")
print(dp[-1][-1])