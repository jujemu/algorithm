import sys
sys.setrecursionlimit(100_001)


input = lambda: sys.stdin.readline().rstrip()
G, P = int(input()), int(input())

parents = ([None] + [i for i in range(1, G+1)])


def find_parent(x):
    if x is None:
        return None

    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(x):
    y = parents[x-1]
    parents[x] = y
    return


answer = 0
for _ in range(P):
    g = int(input())
    result = find_parent(g)
    if result:
        union(result)
        answer += 1
    else:
        break

print(answer)
