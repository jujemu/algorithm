from collections import deque
import sys
import time
sys.stdin = open('./search/input_bj_17472.txt')
input = sys.stdin.readline
current = time.time()

# input
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
num_island = 1
bridge = 'A'
total_island = 0
start = 0 # 섬이 있는 아무 지점
for i in range(N):
    for j in range(M):
        if start:
            break
        if graph[i][j]:
            start = i, j

# dfs
# R, D, L, U
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(x, y):
    graph[x][y] += num_island
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 1:
            dfs(nx, ny)

# traverse, count number of island
# if element of graph is '1', the element is not visited ground
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            dfs(i, j)
            num_island += 1
total_island = max([max(row) for row in graph])

# construct all of available bridge
# horizontal
# full metrix of length of bridge on each island
# 2 ~ 7 
arr = [[M] * 8 for _ in range(8)]
for i in range(N):
    flag, cnt, mark = 0, 0, 0
    for j in range(M):
        if graph[i][j] and not flag:
            flag = graph[i][j]
        
        if flag and not graph[i][j] and not mark:
            mark = j
        
        if flag and not graph[i][j]:
            cnt += 1
            
        if cnt >= 2 and graph[i][j]:
            if arr[flag][graph[i][j]] > cnt:
                arr[flag][graph[i][j]] = cnt
                arr[graph[i][j]][flag] = cnt
                for k in range(mark, j):
                    if not graph[i][k]:
                        graph[i][k] = bridge
                    else:
                        graph[i][k] += bridge
                bridge = chr(ord(bridge) + 1)
            flag, cnt = 0, 0
        elif graph[i][j] and mark:
            flag, cnt = 0, 0

# vertical
# full metrix of length of bridge on each island
# 2 ~ 7 
arr = [[N] * 8 for _ in range(8)]
for j in range(M):
    flag, cnt, mark = 0, 0, 0
    for i in range(N):
        if graph[i][j] and not flag:
            flag = graph[i][j]
        
        if flag and not graph[i][j] and not mark:
            mark = i
        
        if flag and not graph[i][j]:
            cnt += 1
            
        if cnt >= 2 and graph[i][j]:
            if arr[flag][graph[i][j]] > cnt:
                arr[flag][graph[i][j]] = cnt
                arr[graph[i][j]][flag] = cnt
                for k in range(mark, i):
                    if not graph[k][j]:
                        graph[k][j] = bridge
                    else:
                        graph[k][j] += bridge
                bridge = chr(ord(bridge) + 1)
            flag, cnt = 0, 0
        elif graph[i][j] and mark:
            flag, cnt = 0, 0
# print(*graph, sep='\n')

# remove from bridge for optimization
def bfs(x, y, bridge, visited, check):
    q = deque([(x, y, False)])
    cnt = 0
    while q:        
        x, y, dir = q.popleft()
        if dir:
            nx, ny = x + dir[0], y + dir[1]
            if str(graph[nx][ny]).isalpha():
                q.append((nx, ny, dir))
            else:
                q.append((nx, ny, False))
            continue
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M or not graph[nx][ny]:
                continue
            
            if str(graph[nx][ny]).isalpha():
                dir = dx, dy
            else:
                dir = False
                
            if str(graph[nx][ny]).isalpha() and str(graph[nx][ny]) not in bridge:
                continue
            if not visited[nx][ny]:
                if str(graph[nx][ny]).isalpha():
                    cnt += len(graph[nx][ny])
                visited[nx][ny] = True
                q.append((nx, ny, dir))
                if str(graph[nx][ny]) not in check and str(graph[nx][ny]).isnumeric():
                    check += str(graph[nx][ny])      
    if len(check) >= total_island - 1:
            return cnt
    return False

bridge = ' ' + ''.join([chr(ele) for ele in range(ord('A'), ord(bridge))])
def optimizer(bridge):
    result = 100
    visited = [[False] * M for _ in range(N)]
    check = ''
    for idx, _ in enumerate(bridge):
        bridge = list(bridge)
        bridge.pop(idx)
        cnt = bfs(start[0], start[1], ''.join(bridge), visited, check)
        result = min(cnt, result)
        if cnt:
            optimizer(bridge)
        elif not idx:
            return -1
        else:
            return result
print(optimizer(bridge))
