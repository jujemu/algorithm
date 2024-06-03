N = int(input())
road = [c for c in input()]

answer = 0
visited = [False] * N


def seacrh(i):
    global answer

    q = set()
    while True:
        visited[i] = True
        q.add(i)
        cur_n = road[i]
        i = i-1 if cur_n == "W" else i+1
        if visited[i]:
            if i in q:
                answer += 1
            return


for idx, _ in enumerate(road):
    if not visited[idx]:
        seacrh(idx)
print(answer)
