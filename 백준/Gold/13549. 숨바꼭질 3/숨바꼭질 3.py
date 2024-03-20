from collections import deque


N, K = map(int, input().split())

n = 200_000
answer = n
visited = [False] * n
q = deque([(N, 0)])
while q:
    p, time = q.popleft()

    if visited[p]:
        continue

    visited[p] = True
    if p == K:
        answer = min(answer, time)

    # 2배 위치로
    np = p*2
    while np < n and not visited[np]:
        q.append((np, time))
        np *= 2

    np_1, np_2 = p-1, p+1
    if 0 <= np_1 < n and not visited[np_1]:
        q.append((np_1, time+1))
    if 0 <= np_2 < n and not visited[np_2]:
        q.append((np_2, time+1))

print(answer)
