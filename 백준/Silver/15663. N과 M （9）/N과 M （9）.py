import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = []

def bt(cur, cur_indexes):
    if len(cur) == M:
        result.append(cur[:])
        return

    for idx, number in enumerate(numbers):
        if idx not in cur_indexes:
            cur.append(number)
            cur_indexes.append(idx)
            bt(cur, cur_indexes)
            cur.pop()
            cur_indexes.pop()

bt([], [])
result.sort()

prev = None
for r in result:
    if prev != r:
        print(*r, sep=" ")
    prev = r
