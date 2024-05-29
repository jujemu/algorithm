H, W = map(int, input().split())
blocks = [*map(int, input().split())]

answer = 0
# visited = [[0]*W for _ in range(H)]
for i in range(1, H+1):
    pre_j, j = None, 0
    while j < W:
        if i <= blocks[j]:
            if pre_j is not None:
                answer += j - pre_j - 1
                # visited[i-1][pre_j] = j
            pre_j = j

            # if i > 1 and visited[i-2][j] > 0:
            #     j = visited[i-2][j]
            #     continue
        j += 1

print(answer)