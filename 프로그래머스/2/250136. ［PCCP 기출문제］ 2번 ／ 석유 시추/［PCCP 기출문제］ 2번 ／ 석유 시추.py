from collections import defaultdict
import sys
sys.setrecursionlimit(250_000)

color = [0]
N = 500
visited = [[False]*N for _ in range(N)]
oil = defaultdict(int)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(land):    
    r, c = len(land), len(land[0])
    
    for i in range(r):
        for j in range(c):
            if land[i][j] and not visited[i][j]:
                color[0] += 1
                dfs(i, j, land, r, c)
    
    max_value = 0
    for j in range(c):
        cur_sum = calculate_oil(j, land, r)
        max_value = max(max_value, cur_sum)
    
    return max_value


def dfs(i, j, land, r, c):
    if visited[i][j]:
        return
    
    oil[color[0]] += 1
    land[i][j] = color[0]
    visited[i][j] = True
    for d in range(4):
        nx, ny = i+dx[d], j+dy[d]
        if 0 <= nx < r and 0 <= ny < c and land[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny, land, r, c)


def calculate_oil(column, land, r):
    result = 0
    unique = set()
    
    for i in range(r):
        if land[i][column] not in unique:
            unique.add(land[i][column])
            result += oil[land[i][column]]
    
    return result
    