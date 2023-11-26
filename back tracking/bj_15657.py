import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = []

def bt(cur):
    if len(cur) == M:
        result.append(cur[:])
        return

    for number in numbers:
        if not cur or cur[-1] <= number:
            cur.append(number)
            bt(cur)
            cur.pop()

bt([])
result.sort()
for r in result:
    print(*r, sep=" ")
