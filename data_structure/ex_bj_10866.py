from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]
q = deque([])

for cmd in arr:
    if cmd[:10] == "push_front":
        q.appendleft(cmd.split()[1])
    elif cmd[:9] == "push_back":
        q.append(cmd.split()[1])
    elif cmd[:4] == "size":
        print(len(q))
    elif q and cmd[:5] == "empty":
        print(0)

    elif q:
        if cmd[1] == "a":
            print(q[-1])
        elif cmd[1] == "r":
            print(q[0])
        elif cmd[4] == "f":
            print(q.popleft())
        elif cmd[4] == "b":
            print(q.pop())
    else:
        if cmd[:5] == "empty":
            print(1)
        else:
            print(-1)


