N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_length = N+1
p_1, p_2 = 0, 0
cur_sum = sum(arr[p_1:p_2+1])
for _ in range(N*2):
    if cur_sum >= S:
        min_length = min(min_length, p_2-p_1+1)
        cur_sum -= arr[p_1]
        p_1 += 1
        continue

    if p_2 < N-1:
        p_2 += 1
        cur_sum += arr[p_2]

print(min_length if min_length < N+1 else 0)