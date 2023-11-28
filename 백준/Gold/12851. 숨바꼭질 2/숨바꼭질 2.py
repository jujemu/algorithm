from collections import deque

N, K = map(int, input().split())
visited = [False] * 100_001

def move(cur):
    return [cur-1, cur+1, cur*2]

def bfs():
    global result_cnt, result_case
    q = deque([[N, 0]])
    while q:
        cur_idx, cur_cnt = q.popleft()
        if cur_idx == K:
            if cur_cnt == result_cnt:
                result_case += 1

            if not result_cnt:
                result_cnt = cur_cnt
                result_case = 1

        visited[cur_idx] = True

        for n_cur in move(cur_idx):
            if 0 <= n_cur <= 100_000 and not visited[n_cur]:
                q.append([n_cur, cur_cnt+1])

result_cnt, result_case = 0, 0
bfs()
print(result_cnt, result_case, sep="\n")