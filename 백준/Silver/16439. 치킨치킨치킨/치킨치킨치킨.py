def combination(arr, r, s):
    if len(s) == r:
        yield s[:]
        return

    smallest = s[-1] if s else -1
    for ele in arr:
        if smallest < ele:
            s.append(ele)
            yield from combination(arr, r, s)
            s.pop()


N, M = map(int, input().split())
prefers = [
    list(map(int, input().split()))
    for _ in range(N)
]

answer = 0

for a, b, c in combination(range(M), 3, []):
    case_sum = 0
    for n in range(N):
        case_sum += max(prefers[n][a], prefers[n][b], prefers[n][c])
    answer = max(answer, case_sum)
print(answer)
