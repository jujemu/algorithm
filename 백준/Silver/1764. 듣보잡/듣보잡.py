import sys


input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
듣도 = set(
    input() for _ in range(N)
)
보도 = sorted([
    input() for _ in range(M)
])

answer = []
i = 0
for s in 보도:
    if s in 듣도:
        answer.append(s)
print(len(answer))
print(*answer, sep="\n")