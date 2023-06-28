import sys
import time
sys.stdin = open('./search/input_bj_1987.txt')
input = sys.stdin.readline
current = time.time()

# input
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
graph_tmp = [[0] * C for _ in range(R)]

# parameter
A = ord('A')
x, y = 0, 0
cnt = 1
max_cnt = 0
stack = [
    (x, y, cnt, 1 << ord(graph[x][y]) - A)
    ]

# traverse
# U, R, D, L
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while stack:
    x, y, cnt, alphas = stack.pop()
    max_cnt = max(max_cnt, cnt)
    if max_cnt >= 26:
            break        
            
    for dx, dy in d:
        nx, ny = x + dx, y + dy        
        
        # out of graph        
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        
        alpha = 1 << ord(graph[nx][ny]) - A
        # overlap alphas in depth
        if alpha & alphas:
            continue        
        
        tmp = alphas | alpha
        if graph_tmp[nx][ny] != tmp:
            graph_tmp[nx][ny] = tmp
            stack.append((nx, ny, cnt+1, tmp))    

# output
print(max_cnt)
print('processing time is :', time.time() - current)
