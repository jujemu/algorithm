A, B = input(), input()
A = " " + A
B = " " + B

len_a, len_b = len(A), len(B)
dp = [[0]*len_b for _ in range(len_a)]
for r in range(len_a):
    for c in range(len_b):
        if r == 0 or c == 0:
            continue

        if A[r] == B[c]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])

# find max
result = max([max(row) for row in dp])
print(result)
