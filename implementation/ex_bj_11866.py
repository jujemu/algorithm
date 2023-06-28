# input
N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = []

idx = -1
while arr:
    idx += K
    if idx >= len(arr):
        idx %= len(arr)
    result.append(arr.pop(idx))
    idx -= 1
print('<', end='')
print(*result, sep=', ', end='>')