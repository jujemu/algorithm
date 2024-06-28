import sys
input = sys.stdin.readline
s = set()
for _ in range(int(input())):
    s.add(input().rstrip())
print(*sorted(s, key=lambda x: (len(x), x)), sep='\n')