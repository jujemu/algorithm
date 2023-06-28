from collections import deque

def bfs(graph, vertex, visited):
    q = deque(str(vertex))
    visited[vertex] = True
    print(vertex, end=' ')

    while q:
        for adj in graph[int(q.popleft())]:
            if not visited[adj]:
                print(adj, end=' ')
                visited[adj] = True
                q.append(adj) 


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
bfs(graph, 1, visited)