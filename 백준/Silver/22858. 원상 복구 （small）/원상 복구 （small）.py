N, K = map(int, input().split())
S = [*map(int, input().split())]
D = [*map(int, input().split())]

for _ in range(K):
    pre_S = [0 for _ in range(N)]
    for i, s in enumerate(S):
        d = D[i] - 1
        pre_S[d] = s
    S = pre_S
print(*S)