import sys
sys.setrecursionlimit(50**2+1)
input = lambda: sys.stdin.readline().rstrip()

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 국경선
def get_block():
    # 동 서 남 북
    cur_block = [[[False]*4 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if r+1 < N and L <= abs(A[r][c] - A[r+1][c]) <= R:
                cur_block[r][c][2] = True
            if c+1 < N and L <= abs(A[r][c] - A[r][c+1]) <= R:
                cur_block[r][c][0] = True
            if 0 <= r-1 and L <= abs(A[r][c] - A[r-1][c]) <= R:
                cur_block[r][c][3] = True
            if 0 <= c-1 and L <= abs(A[r][c] - A[r][c-1]) <= R:
                cur_block[r][c][1] = True
    return cur_block

def check_block(cur_block):
    for r in range(N):
        for c in range(N):
            if sum(cur_block[r][c]):
                return True
    return False

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def dfs(r, c, cur_block):
    global sm, cnt
    visited[r][c] = True
    
    for idx, cur in enumerate(cur_block[r][c]):
        if cur:
            nr, nc = r+dr[idx], c+dc[idx]
            if not visited[nr][nc]:
                cnt += 1
                sm += A[nr][nc]
                queue.append([nr, nc])
                dfs(nr, nc, cur_block)

result = 0
while True:
    cur_block = get_block()
    if not check_block(cur_block):
        break
    
    result += 1
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                sm, cnt, queue = A[r][c], 1, [[r, c]]
                dfs(r, c, cur_block)
                people = sm // cnt
                for q in queue:
                    A[q[0]][q[1]] = people
print(result)