import sys
sys.setrecursionlimit(100_000)


def dfs(curr):
    members.append(curr)

    n_member = arr[curr]
    visited[curr] = True
    if visited[n_member]:
        if n_member in members:
            selected.extend(members[members.index(n_member):])
            return

    else:
        dfs(n_member)


input = lambda: sys.stdin.readline().rstrip()
answer = []
for _ in range(int(input())):
    n = int(input())
    arr = list(map(lambda x: int(x)-1, input().split()))

    selected = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            members = []
            dfs(i)

    answer.append(n - len(selected))

print(*answer, sep="\n")