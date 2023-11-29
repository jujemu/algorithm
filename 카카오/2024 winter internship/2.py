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
    
    # dfs로 첫 노드를 방문 처리 하지 않았을 때
    # 방문 안 한 노드는 추가된 노드이거나 막대의 첫 노드이다.
    # 조건에 의하면
    visited = [False] * max_number
    for idx in range(1, max_number):
        dfs(idx, visited, grid)
    
    target = 0
    check_visited = [False] * max_number
    for idx in range(1, max_number):
        if not visited[idx]:
            if not pre_grid[idx]:
                pass


    return answer

def dfs(start, visited, grid):
    for adj in grid[start]:
        if not visited[adj]:
            visited[adj] = True
            dfs(adj, visited, grid)