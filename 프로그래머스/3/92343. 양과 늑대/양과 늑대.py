def solution(info, edges):
    global answer
    answer = 0
    
    grid = [[] for _ in range(len(info))]
    for a, b in edges:
        grid[a].append(b)

    init_next_list = [False] * len(info)
    for adj in grid[0]:
        init_next_list[adj] = True
    
    dfs(0, init_next_list, [0,0], grid, info) 
    
    return answer

def dfs(cur_node, next_list, sheep_wolf, grid, info):
    global answer
    next_list[cur_node] = False
    
    if info[cur_node]:
        sheep_wolf[1] += 1
    else:
        sheep_wolf[0] += 1
    
    if sheep_wolf[0] - sheep_wolf[1] <= 0:
        return
    
    if answer < sheep_wolf[0]:
        answer = sheep_wolf[0]
    
    for adj in grid[cur_node]:
        next_list[adj] = True
    
    for idx in range(len(info)):
        if next_list[idx]:
            tmp = tuple(sheep_wolf)
            dfs(idx, next_list, sheep_wolf, grid, info)
            next_list[idx] = True
            sheep_wolf = list(tmp)
    
    for adj in grid[cur_node]:
        next_list[adj] = False
        