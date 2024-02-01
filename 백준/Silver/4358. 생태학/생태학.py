'''
https://www.acmicpc.net/problem/4358

'''
from collections import defaultdict
import sys

# sys.stdin = open("./test.txt")
population = [s.rstrip() for s in sys.stdin]

d = defaultdict(int)
for species in population:
    d[species] += 1

for species in sorted(d):
    print(species, f"{d[species]/len(population)*100:.4f}")
