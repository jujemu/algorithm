import sys
sys.setrecursionlimit(10001)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, visited):
  visited[x][y] = True

  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not grid[nx][ny]:
      dfs(nx, ny, visited)

def get_out():
  visited = [[False]*M for _ in range(N)]
  dfs(0, 0, visited)
  return visited
        
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
  grid_sum = 0
  for r in grid:
    grid_sum += sum(r)
  if grid_sum == 0:
    break
  out = get_out()
  
  for x in range(N):
    for y in range(M):
      if grid[x][y] == 1:
        adj = 0
        for i in range(4):
          nx, ny = x+dx[i], y+dy[i]
          if out[nx][ny]:
            adj += 1
        if adj >= 2:
          grid[x][y] = 0
  time += 1
  
print(time)