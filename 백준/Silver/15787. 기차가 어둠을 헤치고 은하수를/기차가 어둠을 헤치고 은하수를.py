import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
NUMBER_OF_CHAIR = 20

trains = [[False]* (NUMBER_OF_CHAIR + 1) for _ in range(N)]
for _ in range(M):
    c = list(map(int, input().split()))
    c[1] -= 1
    if c[0] == 1:
        trains[c[1]][c[2]] = True
    elif c[0] == 2:
        trains[c[1]][c[2]] = False
    elif c[0] == 3:
        for idx in range(NUMBER_OF_CHAIR-1, 0, -1):
            trains[c[1]][idx+1] = trains[c[1]][idx]
        trains[c[1]][1] = False
    else:
        for idx in range(2, NUMBER_OF_CHAIR+1):
            trains[c[1]][idx-1] = trains[c[1]][idx]
        trains[c[1]][-1] = False
            
s = set()
result = 0
for train in trains:
    value2binary = 0
    for i in range(1, NUMBER_OF_CHAIR+1):
        value2binary += train[i] * 2**(i-1)
    if value2binary not in s:
        s.add(value2binary)
        result += 1
print(result)