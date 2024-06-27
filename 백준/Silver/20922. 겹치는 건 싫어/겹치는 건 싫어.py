N, K = map(int, input().split())
arr = [
    *map(int, input().split())
]

cnt = [0] * 100_001

p1 = 0
for i in range(K):
    cnt[arr[i]] += 1

answer = K
for p2 in range(K, N):
    cnt[arr[p2]] += 1
    while cnt[arr[p2]] > K:
        cnt[arr[p1]] -= 1
        p1 += 1
    answer = max(answer, p2-p1+1)
print(answer)
