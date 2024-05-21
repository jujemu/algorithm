from collections import defaultdict
import sys


input = lambda: sys.stdin.readline().rstrip() 


d = defaultdict(int)
for _ in range(int(input())):
    ext = input().split(".")[1]
    d[ext] += 1

for k in sorted(d.keys()):
    print(f"{k} {d[k]}")