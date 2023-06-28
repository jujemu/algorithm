from collections import deque
import sys
sys.stdin = open('data_structure/input_bj_18258.txt')
input = sys.stdin.readline

q = deque()
for _ in range(int(input().strip())):
    cmd = input().strip()
    if cmd == 'front':
        print(q[0] if q else -1)
    elif cmd == 'back':
        print(q[-1] if q else -1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0 if q else 1)
    elif cmd == 'pop':
        print(int(q.popleft()) if q else -1)
    else:
        q.append(int(cmd.split()[-1]))
    # print(q)
        