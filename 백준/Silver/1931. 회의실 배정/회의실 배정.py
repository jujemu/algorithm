import sys


input = lambda: sys.stdin.readline().rstrip()
N = int(input())
table = [tuple(map(int, input().split())) for _ in range(N)]
table.sort()

answer = 0
min_end = -1
for s, e in table:
    if min_end <= s:
        min_end = e
        answer += 1
        continue
    
    min_end = min(min_end, e)

print(answer)