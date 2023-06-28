import sys
sys.stdin = open('./search/input_bj_11725.txt')
input = sys.stdin.readline

N = int(input())
visit = [False] * (N+1)
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

result = [0]*(N+1)

# dfs
def dfs(vertex):
    for adj in g[vertex]:
        if not visit[adj]:
            visit[adj] = True
            result[adj] = vertex
            dfs(adj)

# traverse
dfs(1)

# output
print(*result[2:], sep='\n')
