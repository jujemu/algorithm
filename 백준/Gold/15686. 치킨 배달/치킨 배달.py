"""
https://www.acmicpc.net/problem/15686

"""
from collections import defaultdict
from itertools import combinations
import sys


input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
town = [tuple(map(int, input().split())) for _ in range(N)]

# 가정집과 치킨집을 저장
houses, bbq = [], []
for i in range(N):
    for j in range(N):
        cur = town[i][j]
        if cur == 1:
            houses.append((i, j))
        elif cur == 2:
            bbq.append((i, j))

# 각 가정집에서 치킨집까지의 거리를 저장
# house_dists: dict
# (distance, (house row, house col)
house_dists = defaultdict(list)
for r, c in houses:
    for i, j in bbq:
        dist = abs(r-i) + abs(c-j)
        house_dists[(r, c)].append((dist, (i, j)))

# 가정집에서 치킨집까지의 거리를 기준으로 오름차순 정렬
for r, c in house_dists:
    house_dists[(r, c)].sort()

def opening():
    for i in range(N):
        for j in range(N):
            open_bbqs[i][j] = False

    for i, j in comb:
        open_bbqs[i][j] = True


min_dist = int(1e9)
open_bbqs = [[False]*N for _ in range(N)]
for comb in combinations(bbq, M):
    opening()

    result = 0
    for r, c in houses:
        for dist, (i, j) in house_dists[r, c]:
            if open_bbqs[i][j]:
                result += dist
                break
    min_dist = min(min_dist, result)
print(min_dist)
