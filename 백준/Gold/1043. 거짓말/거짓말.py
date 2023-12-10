import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
known = set(map(int, input().split()[1:]))

parents = [None] + [i for i in range(1, N+1)]


def find_parent(child):
    if parents[child] != child:
        parents[child] = find_parent(parents[child])
    return parents[child]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def check_known(party):
    for p in party:
        if find_parent(p) in known:
            return False
    return True


parties = []
for _ in range(M):
    party = list(map(int, input().split()[1:]))
    if len(party) != 1:
        for idx, p in enumerate(party[1:], start=1):
            union(party[idx - 1], party[idx])
    parties.append(party)

tmp = set()
for k in known:
    k_parent = find_parent(k)
    tmp.add(k_parent)
known |= tmp

result = 0
for party in parties:
    if check_known(party):
        result += 1
print(result)

