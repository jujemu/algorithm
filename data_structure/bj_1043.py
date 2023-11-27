import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
knowns = set(map(int, input().split()[1:]))
party = [list(map(int, input().split()[1:])) for _ in range(M)]
visited = [False] * (N+1)

q = list(knowns)
while q:
    known = q.pop()
    visited[known] = True
    
    for attendees in party:
        if known in attendees:
            for attendee in attendees:
                if not visited[attendee]:
                    knowns.add(attendee)
                    q.append(attendee)

result = 0
for attendees in party:
    flag = True
    for known in knowns:
        if known in attendees:
            flag = False
            break
    if flag:
        result += 1

print(result)