import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = []

a_idx, b_idx = 0, 0
while True:
    if a_idx >= N:
        result.extend(B[b_idx:])
        break
    if b_idx >= M:
        result.extend(A[a_idx:])
        break

    if A[a_idx] >= B[b_idx]:
        result.append(B[b_idx])
        b_idx += 1
        continue
    result.append(A[a_idx])
    a_idx += 1
print(*result, sep=" ")