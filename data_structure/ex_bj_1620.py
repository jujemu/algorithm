import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poks = {input().rstrip(): i for i in range(1, N+1)}
key = list(poks.keys())

for _ in range(M):
    m = input().rstrip()
    if m.isdigit():
        print(key[int(m)-1])
    else:
        print(poks[m])