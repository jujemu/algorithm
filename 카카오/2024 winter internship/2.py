# import sys
# sys.setrecursionlimit(10*6+1)

def solution(edges):
    answer = []

    max_number = 0
    grid = [[] for _ in range(1_000_001)]
    pre_grid = [[] for _ in range(1_000_001)]
    for edge in edges:
        a, b = edge
        grid[a].append(b)
        pre_grid[b].append(a)
        if a > max_number:
            max_number = a
        if b > max_number:
            max_number = b
    grid = grid[:max_number+1]
    pre_grid = pre_grid[:max_number+1]
    
    # 방문 안 한 노드는 추가된 노드이거나 막대의 첫 노드이다.
    # 막대의 첫 노드는 방문이 될 수도, 안 될 수도 있다.
    # 막대의 첫 노드는 하나의 노드만을 가리킨다.
    # 만약 추가된 노드가 막대 그래프만을 가리키는 것이 아니라면
    # 방문하지 않은 노드들 중에 하나의 노드만을 가리키는 것은 반드시 막대 그래프의 첫 노드이다.
    visited = [False] * max_number
    for idx in range(1, max_number):
        dfs(idx, visited, grid)
    
    target = 0
    check_visited = [False] * max_number
    for idx in range(1, max_number):
        if not visited[idx]:
            if not pre_grid[idx]:


    return answer

def dfs(start, visited, grid):
    for adj in grid[start]:
        if not visited[adj]:
            visited[adj] = True
            dfs(adj, visited, grid)