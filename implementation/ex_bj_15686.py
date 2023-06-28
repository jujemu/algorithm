from itertools import combinations
import sys
sys.stdin = open('./implementation/input_bj_15686.txt')
input = sys.stdin.readline

# input
N, M = map(int, input().split())
# graph = [list(map(int, input().rstrip().split())) for _ in range(N)] # '0' is empty, '1' is house, '2' is fried chicken joint
graph = []
houses, chick_place = [], []
for i in range(N):
    tmp = list(map(int, input().rstrip().split()))
    graph.append(tmp)
    for idx, j in enumerate(tmp):
        if j == 2:
            chick_place.append((i, idx))
        elif j == 1:
            houses.append((i, idx))
# print(*graph, sep='\n')
# print(*chick_place, sep='\n')

# list of each houses which includes distance of fried chicken places
dist_list = [[] for _ in range(len(houses))]
for idx, house in enumerate(houses):
    for chick in chick_place:
        dist = abs(chick[0] - house[0]) + abs(chick[1] - house[1])
        dist_list[idx].append(dist)
# print(*dist_list, sep='\n')

cases = list(combinations(range(len(chick_place)), M))
total = [0 for _ in range(len(cases))]
for case_idx, case in enumerate(cases):    
    for dist in dist_list:
        mn = 999999
        for i in case:
            mn = min(mn, dist[i])
        total[case_idx] += mn

print(min(total))
