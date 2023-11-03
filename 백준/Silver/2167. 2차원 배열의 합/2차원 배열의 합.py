N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
K = [list(map(int, input().split())) for _ in range(K)]
for k in K:
    i, j, x, y = k
    s = 0

    for a in [ar[j-1:y] for ar in arr[i-1:x]]:
        s += sum(a)
    print(s)