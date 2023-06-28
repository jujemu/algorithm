def dfs(g, vertex, visited):
    print(vertex, end=' ')
    visited[vertex] = True
    for adj in graph[vertex]:
        if not visited[adj]:
            dfs(g, adj, visited)


# element of graph is sorted ASC
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)