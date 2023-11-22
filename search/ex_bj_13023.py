import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(2001)

N, M = map(int, input().split())
relation = [[] for _ in range(N)]
for _ in range(M):
    p_1, p_2 = map(int, input().split())
    relation[p_1].append(p_2)
    relation[p_2].append(p_1)

def dfs(i, cnt, visited):
    if cnt == 4:
        return True

    visited.append(i)
    for friend in relation[i]:
        if friend not in visited:
            if dfs(friend, cnt+1, visited):
                return True
    visited.pop()
    return False

def solve():
    for i in range(N):
        visited = []
        if dfs(i, 0, visited):
            return 1
    return 0
print(solve())
