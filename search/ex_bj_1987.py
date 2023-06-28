import sys
import time
sys.stdin = open('./search/input_bj_1987.txt')
input = sys.stdin.readline
current = time.time()

# U, D, L, R
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def dfs(v, cnt=0):
    x, y = v
    cnt += 1
    alphas[ord(graph[y][x]) - ord('A')] = 1
    
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= C or ny < 0 or ny >= R or (alphas[ord(graph[ny][nx]) - ord('A')]):
            continue    
        v = nx, ny
        dfs(v, cnt)
        alphas[ord(graph[ny][nx]) - ord('A')] = 0
    global max_cnt
    max_cnt = max(max_cnt, cnt)
            

# input
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
alphas = [0] * 26
start = (0, 0)

# output
max_cnt = 0 # global variable
dfs(start)
print(max_cnt)
# print(time.time() - current)
