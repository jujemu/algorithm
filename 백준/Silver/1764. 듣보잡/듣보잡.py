import sys


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
듣도 = [
    input() for _ in range(n)
]
보도 = [
    input() for _ in range(m)
]

result = set(듣도) & set(보도)
print(len(result))
print(*sorted(
    result
), sep="\n")