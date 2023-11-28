result = []
for _ in range(int(input())):
    H, W, N = map(int, input().split())
    result.append(str((N-1) % H +1) + "{:02d}".format((N-1) // H + 1))
print(*result, sep="\n")