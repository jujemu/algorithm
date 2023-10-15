import sys
input = lambda: sys.stdin.readline().rstrip()

# 입력
N = int(input())
order = []
likes = [[] for _ in range(N**2 + 1)]
for i in range(N**2):
    get = list(map(int, input().split()))
    likes[get[0]].extend(get[1:])
    order.append(get[0])

g = [[0] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
def con1(like):
    mx = -1
    mx_list = []
    for i in range(N):
        for j in range(N):
            if g[i][j]:
                continue

            cur_like = 0
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if g[nx][ny] in like:
                        cur_like += 1
            if cur_like >= mx:
                if cur_like > mx:
                    mx_list = []
                mx = cur_like
                mx_list.append((i, j))
    
    return mx_list

# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
def con2(mx_list):
    empty_mx = -1
    empty_list = []
    for mx in mx_list:
        i, j = mx
        cur_empty_mx = 0
        for d in range(4):
            nx, ny = i+dx[d], j+dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if g[nx][ny] == 0:
                    cur_empty_mx += 1
        if empty_mx <= cur_empty_mx:
            if empty_mx < cur_empty_mx:
                empty_list = []
            empty_mx = cur_empty_mx
            empty_list.append((i, j))

    return empty_list

# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
def con3(empty_list):
    empty_list.sort()

    return empty_list[0]

# 만족도 구하기
def sumSatisfied():
    s = 0

    for i in range(N):
        for j in range(N):
            cur = g[i][j]

            personal_satisfy = 0
            for d in range(4):
                nx, ny = i+dx[d], j+dy[d]

                if 0 <= nx < N and 0 <= ny < N:
                    if g[nx][ny] in likes[cur]:
                        personal_satisfy += 1
            s += 10 ** (personal_satisfy-1) if personal_satisfy else 0
    return s


for o in order:
    result = con1(likes[o])
    # print("첫 번째 결과: ", result)
    if len(result) == 1:
        result = result[0]
        g[result[0]][result[1]] = o
        continue
    
    result = con2(result)
    # print("두 번째 결과: ", result)

    if len(result) == 1:
        result = result[0]
        g[result[0]][result[1]] = o
        continue

    result = con3(result)
    # print("세 번째 결과: ", result)
    g[result[0]][result[1]] = o

# print(*g, sep="\n")
# print(order)
# print(*likes, sep="\n")
print(sumSatisfied())
